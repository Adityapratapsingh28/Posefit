from flask import Flask, Response, render_template
import cv2
import mediapipe as mp
import numpy as np

app = Flask(__name__)

# Initialize MediaPipe
mp_holistic = mp.solutions.holistic
mp_drawing = mp.solutions.drawing_utils

# Function to calculate angle
def calculate_angle(a, b, c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)
    return 360 - angle if angle > 180.0 else angle

# Initialize Variables
counter = 0
stage = None
started = False
prev_angle = 0
CURL_DOWN_ANGLE = 150  
CURL_UP_ANGLE = 70   
SMOOTHING_FACTOR = 0.5 

cap = cv2.VideoCapture(0)

def generate_frames():
    global counter, stage, started, prev_angle
    
    with mp_holistic.Holistic(min_detection_confidence=0.7, min_tracking_confidence=0.7) as holistic:
        while True:
            success, frame = cap.read()
            if not success:
                break
            
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = holistic.process(image)
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            try:
                if results.pose_landmarks:
                    shoulder = [results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_SHOULDER].x,
                                results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_SHOULDER].y]
                    elbow = [results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_ELBOW].x,
                             results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_ELBOW].y]
                    wrist = [results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_WRIST].x,
                             results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_WRIST].y]
                    
                    current_angle = calculate_angle(shoulder, elbow, wrist)
                    smoothed_angle = (current_angle * SMOOTHING_FACTOR) + (prev_angle * (1 - SMOOTHING_FACTOR))
                    prev_angle = smoothed_angle

                    if not started and smoothed_angle > CURL_DOWN_ANGLE:
                        started = True
                        stage = 'down'
                    
                    if started:
                        if stage == 'down' and smoothed_angle < CURL_UP_ANGLE:
                            stage = 'up'
                        elif stage == 'up' and smoothed_angle > CURL_DOWN_ANGLE:
                            stage = 'down'
                            counter += 1

                    color = (255, 0, 0) if stage == 'down' else (0, 255, 0)
                    cv2.putText(image, f'Angle: {int(smoothed_angle)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

                    mp_drawing.draw_landmarks(
                        image,
                        results.pose_landmarks,
                        mp_holistic.POSE_CONNECTIONS,
                        mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                        mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2)
                    )
                    
            except Exception as e:
                print(f"Error: {e}")

            cv2.putText(image, f'Reps: {counter}', (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            cv2.putText(image, f'Stage: {stage}', (10, 130), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

            _, buffer = cv2.imencode('.jpg', image)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True, port=3030)
