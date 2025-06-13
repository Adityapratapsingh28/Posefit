import cv2
import mediapipe as mp
import numpy as np
import pyttsx3
import mysql.connector
import time

# Initialize MediaPipe
mp_holistic = mp.solutions.holistic
mp_drawing = mp.solutions.drawing_utils

# Initialize Text-to-Speech
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speech speed

def speak(text):
    """Function to speak a given text."""
    engine.say(text)
    engine.runAndWait()

def calculate_angle(a, b, c):
    """Calculate angle between three points"""
    a, b, c = np.array(a), np.array(b), np.array(c)
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)
    return 360 - angle if angle > 180 else angle

# Database Connection
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Your MySQL username
        password="root",  # Your MySQL password
        database="aithelete"
    )

# User Login/Signup
def login():
    db = connect_db()
    cursor = db.cursor()

    print("\n1. Login\n2. Signup")
    choice = input("Select (1/2): ")

    if choice == "1":  # Login
        email = input("Enter Email: ")
        password = input("Enter Password: ")

        cursor.execute("SELECT User_id FROM users WHERE email = %s AND password = %s", (email, password))
        result = cursor.fetchone()

        if result:
            print("✅ Login Successful!")
            return result[0]  # Return user_id
        else:
            print("❌ Invalid credentials.")
            return None

    elif choice == "2":  # Signup
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        password = input("Enter Password: ")
        weight = float(input("Enter Weight: "))
        age = int(input("Enter Age: "))
        gender = input("Enter Gender: ")

        cursor.execute("INSERT INTO users (name, email, password, weight, Age, gender) VALUES (%s, %s, %s, %s, %s, %s)",
                       (name, email, password, weight, age, gender))
        db.commit()

        print("✅ Signup Successful! Please login.")
        return None
    
    db.close()
    return None

# Function to display exercise selection menu
def select_exercise():
    print("\nSelect Exercise:\n1. Squats\n2. Bicep Curls\n3. Pushups")
    choice = input("Choose (1/2/3): ")

    exercises = {
        "1": "Squats",
        "2": "Bicep Curls",
        "3": "Pushups"
    }

    if choice in exercises:
        return exercises[choice]
    else:
        print("❌ Invalid selection.")
        return None

# Function to run the CV model based on the exercise type
def run_cv_model(user_id, exercise_name):
    if exercise_name == "Bicep Curls":
        reps = run_bicep_curl_counter()
    elif exercise_name == "Squats":
        reps = run_squat_counter()
    elif exercise_name == "Pushups":
        reps = run_pushup_counter()
    else:
        print(f"❌ Exercise {exercise_name} not implemented yet.")
        return
    
    # Store the reps in the workout_plans table
    if reps > 0:
        store_workout(user_id, exercise_name, reps)

# Store workout data in MySQL
def store_workout(user_id, exercise_name, reps):
    try:
        db = connect_db()
        cursor = db.cursor()

        # Get current date/time
        current_date = time.strftime('%Y-%m-%d')
        
        # Insert workout data
        query = """
        INSERT INTO workout_plans 
        (user_id, exercise_name, number_of_reps, workout_date) 
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (user_id, exercise_name, reps, current_date))
        db.commit()

        print(f"✅ Stored {reps} reps for {exercise_name} in the database!")
        db.close()
    except Exception as e:
        print(f"❌ Database error: {e}")

# Bicep Curl Counter Function
def run_bicep_curl_counter():
    # Initialize Variables
    counter = 0
    stage = None
    started = False
    prev_angle = 0
    form_issue = ""

    # Thresholds
    CURL_DOWN_ANGLE = 150
    CURL_UP_ANGLE = 70
    SMOOTHING_FACTOR = 0.5  # Angle smoothing

    # Video capture
    cap = cv2.VideoCapture(0)

    with mp_holistic.Holistic(min_detection_confidence=0.7, min_tracking_confidence=0.7) as holistic:
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Convert BGR to RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = holistic.process(image)
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            try:
                if results.pose_landmarks:
                    # Get coordinates for right arm
                    shoulder = [results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_SHOULDER].x,
                              results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_SHOULDER].y]
                    elbow = [results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_ELBOW].x,
                            results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_ELBOW].y]
                    wrist = [results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_WRIST].x,
                            results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_WRIST].y]
                    
                    # Calculate angle with smoothing
                    current_angle = calculate_angle(shoulder, elbow, wrist)
                    smoothed_angle = (current_angle * SMOOTHING_FACTOR) + (prev_angle * (1 - SMOOTHING_FACTOR))
                    angle = smoothed_angle
                    prev_angle = angle
                    
                    # Form correction logic
                    form_issue = ""
                    if elbow[1] < shoulder[1] - 0.1:  # If elbow is too high
                        form_issue = "Lower your elbow."
                    elif wrist[1] > elbow[1] + 0.1:  # If wrist is too low
                        form_issue = "Keep your wrist aligned."

                    # Improved rep counting logic
                    if not started and angle > CURL_DOWN_ANGLE:
                        started = True
                        stage = 'down'

                    if started:
                        if stage == 'down' and angle < CURL_UP_ANGLE:
                            stage = 'up'
                        elif stage == 'up' and angle > CURL_DOWN_ANGLE:
                            stage = 'down'
                            counter += 1
                            speak(f"Rep {counter}")  # Speak rep count

                    # Voice feedback for form correction
                    if form_issue:
                        speak(form_issue)

                    # Visual feedback
                    color = (255, 0, 0) if stage == 'down' else (0, 255, 0)
                    
                    # Draw arm angle
                    cv2.putText(image, f'Angle: {int(angle)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
                    
                    # Draw landmarks
                    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
                                              mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                              mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2))

            except Exception as e:
                print(f"Error: {e}")

            # Display counter, stage, and form correction
            cv2.putText(image, f'Reps: {counter}', (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            cv2.putText(image, f'Stage: {stage}', (10, 130), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            cv2.putText(image, form_issue, (10, 180), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

            # Add instructions
            cv2.putText(image, 'Stand sideways to camera', (10, image.shape[0] - 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(image, 'Press q to quit', (10, image.shape[0] - 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

            # Show image
            cv2.imshow('Bicep Curl Counter with Voice & Form Correction', image)

            # Break loop
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()
    return counter

# Squat Counter Function (simplified example - you can expand this)
def run_squat_counter():
    # Initialize variables
    counter = 0
    stage = None
    
    # Video capture
    cap = cv2.VideoCapture(0)

    with mp_holistic.Holistic(min_detection_confidence=0.7, min_tracking_confidence=0.7) as holistic:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
                
            # Process frame
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = holistic.process(image)
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            
            try:
                if results.pose_landmarks:
                    # Get hip, knee, and ankle landmarks for squat detection
                    hip = [results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_HIP].y,
                          results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_HIP].x]
                    knee = [results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_KNEE].y,
                           results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_KNEE].x]
                    ankle = [results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_ANKLE].y,
                            results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_ANKLE].x]
                    
                    # Simple squat detection based on knee position
                    if stage == 'down' and knee[0] < hip[0] + 0.1:  # When user stands up
                        stage = 'up'
                        counter += 1
                        speak(f"Rep {counter}")
                    elif stage == 'up' or stage == None:
                        if knee[0] > hip[0] + 0.1:  # When user squats down
                            stage = 'down'
                    
                    # Draw landmarks
                    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)
            except Exception as e:
                print(f"Error: {e}")
                
            # Display counter and stage
            cv2.putText(image, f'Reps: {counter}', (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            cv2.putText(image, f'Stage: {stage}', (10, 130), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            
            # Show instructions
            cv2.putText(image, 'Stand facing the camera', (10, image.shape[0] - 60),
                      cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(image, 'Press q to quit', (10, image.shape[0] - 30),
                      cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                
            # Show image
            cv2.imshow('Squat Counter', image)
            
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
                
    cap.release()
    cv2.destroyAllWindows()
    return counter

# Pushup Counter Function (simplified example - you can expand this)
def run_pushup_counter():
    # Initialize variables
    counter = 0
    stage = None
    
    # Video capture
    cap = cv2.VideoCapture(0)

    with mp_holistic.Holistic(min_detection_confidence=0.7, min_tracking_confidence=0.7) as holistic:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
                
            # Process frame
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = holistic.process(image)
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            
            try:
                if results.pose_landmarks:
                    # Get shoulder, elbow, and wrist landmarks for pushup detection
                    shoulder = [results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_SHOULDER].y,
                               results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_SHOULDER].x]
                    elbow = [results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_ELBOW].y,
                            results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_ELBOW].x]
                    wrist = [results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_WRIST].y,
                            results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_WRIST].x]
                    
                    # Simple pushup detection based on shoulder height
                    if stage == 'down' and shoulder[0] < 0.6:  # When user pushes up
                        stage = 'up'
                        counter += 1
                        speak(f"Rep {counter}")
                    elif stage == 'up' or stage == None:
                        if shoulder[0] > 0.65:  # When user lowers down
                            stage = 'down'
                    
                    # Draw landmarks
                    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)
            except Exception as e:
                print(f"Error: {e}")
                
            # Display counter and stage
            cv2.putText(image, f'Reps: {counter}', (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            cv2.putText(image, f'Stage: {stage}', (10, 130), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            
            # Show instructions
            cv2.putText(image, 'Position camera to see your upper body side view', (10, image.shape[0] - 60),
                      cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(image, 'Press q to quit', (10, image.shape[0] - 30),
                      cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                
            # Show image
            cv2.imshow('Pushup Counter', image)
            
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
                
    cap.release()
    cv2.destroyAllWindows()
    return counter

# Main Function
def main():
    # User login/signup
    user_id = login()
    
    if user_id:
        while True:
            # Select exercise
            exercise_name = select_exercise()
            
            if exercise_name:
                # Run CV model for selected exercise
                run_cv_model(user_id, exercise_name)
            
            # Ask if user wants to continue
            continue_choice = input("\nDo you want to do another exercise? (y/n): ")
            if continue_choice.lower() != 'y':
                break
    
    print("Thank you for using AI Athlete! Stay fit 💪")

if __name__ == "__main__":
    main()