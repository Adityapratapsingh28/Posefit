from flask import Flask, jsonify, render_template, send_from_directory
import os
import json
from datetime import datetime

app = Flask(__name__, static_folder='static', template_folder='templates')

# File to store challenges
CHALLENGES_FILE = 'data/challenges.json'

# Ensure data directory exists
if not os.path.exists('data'):
    os.makedirs('data')

# Initialize challenges or load existing ones
def init_challenges():
    create_new_challenges = True
    
    if os.path.exists(CHALLENGES_FILE):
        try:
            with open(CHALLENGES_FILE, 'r') as f:
                challenges = json.load(f)
            
            # Verify the challenges data is valid and not empty
            if challenges and isinstance(challenges, list) and len(challenges) > 0:
                if isinstance(challenges[0], dict) and "date" in challenges[0]:
                    # Valid challenges exist
                    create_new_challenges = False
                    
                    # Update the date to today to refresh challenges
                    today = datetime.now().strftime("%Y-%m-%d")
                    if challenges[0]["date"] != today:
                        for challenge in challenges:
                            challenge["date"] = today
                        
                        with open(CHALLENGES_FILE, 'w') as f:
                            json.dump(challenges, f)
        except (json.JSONDecodeError, KeyError, IndexError):
            # If any error occurs while reading or processing the file,
            # we'll create new challenges
            pass
    
    if create_new_challenges:
        # Sample daily challenges
        challenges = [
            {
                "id": "d1",
                "title": "Morning Stretch",
                "description": "Complete a 10-minute morning stretch routine to increase flexibility.",
                "points": 10,
                "difficulty": "Easy",
                "date": datetime.now().strftime("%Y-%m-%d")
            },
            {
                "id": "d2",
                "title": "10,000 Steps",
                "description": "Walk at least 10,000 steps today to improve cardiovascular health.",
                "points": 15,
                "difficulty": "Medium",
                "date": datetime.now().strftime("%Y-%m-%d")
            },
            {
                "id": "d3",
                "title": "Hydration Hero",
                "description": "Drink at least 8 glasses of water throughout the day.",
                "points": 10,
                "difficulty": "Easy",
                "date": datetime.now().strftime("%Y-%m-%d")
            },
            {
                "id": "d4",
                "title": "HIIT Workout",
                "description": "Complete a 20-minute high intensity interval training session.",
                "points": 25,
                "difficulty": "Hard",
                "date": datetime.now().strftime("%Y-%m-%d")
            },
            {
                "id": "d5",
                "title": "Healthy Meal",
                "description": "Prepare and eat a balanced, nutritious meal with protein, vegetables, and whole grains.",
                "points": 15,
                "difficulty": "Medium",
                "date": datetime.now().strftime("%Y-%m-%d")
            },
            {
                "id": "d6",
                "title": "Mindful Meditation",
                "description": "Spend 10 minutes meditating to reduce stress and improve mental clarity.",
                "points": 10,
                "difficulty": "Easy",
                "date": datetime.now().strftime("%Y-%m-%d")
            }
        ]
        
        with open(CHALLENGES_FILE, 'w') as f:
            json.dump(challenges, f)
    
    return challenges

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/challenges')
def get_challenges():
    challenges = init_challenges()
    return jsonify(challenges)

# Serve static files
@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    # Make sure the challenges file exists
    init_challenges()
    app.run(debug=True, port=3009)