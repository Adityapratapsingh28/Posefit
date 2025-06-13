import cv2
import mysql.connector
import time

# Database Connection
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",                # Your MySQL username
        password="root",        # Your MySQL password
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

# Function to simulate the Computer Vision Model
def run_cv_model(user_id, exercise_name):
    cap = cv2.VideoCapture(0)

    reps = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Display the reps (dummy CV logic)
        cv2.putText(frame, f"Reps: {reps}", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        cv2.imshow(f"{exercise_name} Tracker", frame)

        key = cv2.waitKey(1)
        if key == ord('q'):   # Press 'q' to quit
            break

        # Simulate reps increment (replace this with your actual CV model logic)
        reps += 1
        time.sleep(1)

    cap.release()
    cv2.destroyAllWindows()

    # Store the reps in the workout_plans table
    store_reps(user_id, exercise_name, reps)

# Store reps in MySQL
def store_reps(user_id, exercise_name, reps):
    db = connect_db()
    cursor = db.cursor()

    query = "INSERT INTO workout_plans (user_id, exercise_name, number_of_reps) VALUES (%s, %s, %s)"
    cursor.execute(query, (user_id, exercise_name, reps))
    db.commit()

    print(f"✅ Stored {reps} reps for {exercise_name} in the database!")

# Main Execution Flow
def main():
    user_id = login()
    if user_id:
        print("\nSelect Exercise:\n1. Squats\n2. Bicep Curls\n3. Pushups")
        choice = input("Choose (1/2/3): ")

        exercises = {
            "1": "Squats",
            "2": "Bicep Curls",
            "3": "Pushups"
        }

        if choice in exercises:
            run_cv_model(user_id, exercises[choice])
        else:
            print("❌ Invalid selection.")

if __name__ == "__main__":
    main()
