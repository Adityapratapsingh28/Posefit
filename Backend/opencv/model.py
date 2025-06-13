import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe
mp_holistic = mp.solutions.holistic
mp_drawing = mp.solutions.drawing_utils

def calculate_angle(a, b, c):
    """
    Calculate angle between three points
    Args:
        a: first point [x, y]
        b: mid point [x, y]
        c: end point [x, y]
    Returns:
        angle in degrees
    """
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)
    
    if angle > 180.0:
        angle = 360 - angle
        
    return angle

# Initialize Variables
counter = 0
stage = None
started = False
prev_angle = 0

# Thresholds
CURL_DOWN_ANGLE = 150  # Angle when arm is extended
CURL_UP_ANGLE = 70    # Angle when arm is curled
SMOOTHING_FACTOR = 0.5  # For angle smoothing

# Video capture
cap = cv2.VideoCapture(0)

with mp_holistic.Holistic(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7) as holistic:

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
            
        # Convert BGR to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Make detection
        results = holistic.process(image)
        
        # Convert back to BGR
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        # Extract landmarks
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
                
                # Visual feedback
                color = (255, 0, 0) if stage == 'down' else (0, 255, 0)
                
                # Draw arm angle
                cv2.putText(image, f'Angle: {int(angle)}', 
                           (10, 30), 
                           cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
                
                # Draw landmarks with custom style
                mp_drawing.draw_landmarks(
                    image,
                    results.pose_landmarks,
                    mp_holistic.POSE_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                    mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2))
                
        except Exception as e:
            print(f"Error: {e}")
            pass
            
        # Display counter and stage
        cv2.putText(image, f'Reps: {counter}', 
                    (10, 80), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.putText(image, f'Stage: {stage}', 
                    (10, 130), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        
        # Add instruction text
        cv2.putText(image, 'Stand sideways to camera', 
                    (10, image.shape[0] - 60), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(image, 'Press q to quit', 
                    (10, image.shape[0] - 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        # Show image
        cv2.imshow('Bicep Curl Counter', image)
        
        # Break loop
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()