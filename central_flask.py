import subprocess
import requests
import time
import os
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import mysql.connector

app = Flask(__name__)

# List of microservice Flask apps with their expected ports
microservices = [
    {"name": "Chatbot", "path": r"D:\DBMS PROJECT\dbms fitness project\Backend\Fitness_chatbot\app.py", "port": 3001},
    {"name": "OpenCV", "path": r"D:\DBMS PROJECT\dbms fitness project\Backend\opencv\app.py", "port": 3030},
    {"name": "Challenges", "path": r"D:\DBMS PROJECT\dbms fitness project\Backend\challenges\app.py", "port": 3009},
    {"name": "Injury", "path": r"D:\DBMS PROJECT\dbms fitness project\Backend\injury\injury_app.py", "port": 5002},
    {"name": "Nutrition", "path": r"D:\DBMS PROJECT\dbms fitness project\Backend\Nutrition_plan\app.py", "port": 3012},
    {"name": "Mental_wellness", "path": r"D:\DBMS PROJECT\dbms fitness project\Backend\MentalWellness\well_app.py", "port": 5001},
]

running_processes = []

def launch_microservices():
    for service in microservices:
        print(f"Launching {service['name']} on port {service['port']}...")
        # Start the service
        process = subprocess.Popen(["python", service["path"]], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        running_processes.append({"process": process, "service": service})

    print("\nWaiting for services to start...\n")
    time.sleep(5)  # Wait a few seconds for services to boot

    for proc in running_processes:
        port = proc["service"]["port"]
        name = proc["service"]["name"]
        try:
            response = requests.get(f"http://127.0.0.1:{port}", timeout=2)
            if response.status_code == 200:
                print(f"✅ {name} is running at http://127.0.0.1:{port}")
            else:
                print(f"⚠️ {name} is not responding properly at http://127.0.0.1:{port}")
        except requests.exceptions.RequestException:
            print(f"❌ {name} is NOT running at http://127.0.0.1:{port}")

launch_microservices()

app.secret_key = 'cd0df92f92f997d5492f59872add022bf6c4473f1fee51ebacd4a76fa38c82ef'

# Helper function to get a DB connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        port=3306,  # Adjust if needed
        user="root",
        password="root",
        database="pose"
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form.get('name')
        email = request.form.get('email')
        age = request.form.get('age')
        gender = request.form.get('gender')
        password = request.form.get('password')
        weight = request.form.get('weight')

        # Simple validation
        if not all([name, email, age, gender, password, weight]):
            flash('Please fill out all fields')
            return redirect(url_for('signup'))

        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            # Insert new user
            query = """
                INSERT INTO users (name, email, age, gender, password, weight)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (name, email, age, gender, password, weight))
            conn.commit()
            flash('Sign up successful!')

        except mysql.connector.Error as err:
            flash(f'Error: {err}')

        finally:
            cursor.close()
            conn.close()

        return redirect(url_for('index'))

    return render_template('signup.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        # Fetch user details based on email
        query = "SELECT * FROM users WHERE email = %s"
        cursor.execute(query, (email,))
        user = cursor.fetchone()

        if user and user['password'] == password:  # Direct comparison for plain text
            return jsonify({"success": True, "message": "Login successful"})
        else:
            return jsonify({"success": False, "message": "Invalid email or password"})

    except mysql.connector.Error as err:
        return jsonify({"success": False, "message": f"Error: {err}"})

    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'conn' in locals() and conn:
            conn.close()

if __name__ == '__main__':
    app.run(debug=True,port=5000)


