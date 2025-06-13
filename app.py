'''import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    port=3306,  # Add this if needed
    user="root",
    password="root",
    database="posefit"  # Ensure correct case
)

cursor = conn.cursor()

# Retrieve Data
cursor.execute("SELECT * FROM EMP")
rows = cursor.fetchall()
for row in rows:
    print(row)  # Prints each row


conn.commit()



# Close connection
cursor.close()
conn.close()


'''



'''

import mysql.connector

def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        port=3306,  # adjust if needed
        user="root",
        password="root",
        database="posefit"
    )
    return conn

def test_login(email, password):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        query = "SELECT * FROM users WHERE email = %s AND password = %s"
        cursor.execute(query, (email, password))
        user = cursor.fetchone()

        if user:
            print("Login successful!")
        else:
            print("Invalid email or password!")
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally:
        cursor.close()
        conn.close()

# Test case
test_login("root@gmail.com", "root")'''
from flask import Flask, render_template, request, redirect, url_for, flash,jsonify
import mysql.connector

app = Flask(__name__)
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
    app.run(debug=True, port=5000)
