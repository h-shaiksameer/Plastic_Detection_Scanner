from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from threading import Thread
import plastic_detection
from werkzeug.utils import secure_filename
import analyse
from flask import send_from_directory
import os
import json
import time
from report import *

app = Flask(__name__)

# Thread variable
scan_thread = None
app.secret_key = os.urandom(24)  # Generates a random secret key


app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['REPORT_FOLDER'] = 'reports'
USERS_FILE = 'users.json'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

if not os.path.exists(app.config['REPORT_FOLDER']):
    os.makedirs(app.config['REPORT_FOLDER'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg'}

if not os.path.exists(USERS_FILE):
    with open(USERS_FILE, 'w') as f:
        json.dump({}, f)  # Create empty users.json


# 🔹 Helper Function: Load Users
def load_users():
    with open(USERS_FILE, 'r') as f:
        return json.load(f)


# 🔹 Helper Function: Save Users
def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=4)


# ✅ Route: Register User
@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    users = load_users()

    if email in users:
        return render_template('register.html', error="User already exists!")

    users[email] = {"name": name, "password": password}
    save_users(users)

    return redirect(url_for('login'))

@app.route('/register', methods=['GET'])
def register_page():
    return render_template('register.html')


# ✅ Route: Login User
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        users = load_users()

        if email in users and users[email]['password'] == password:
            session['user'] = email  # Store user session
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error="Invalid credentials!")

    return render_template('login.html')


# ✅ Route: Logout User
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))


# ✅ Protected Route: Index (Only Logged-in Users)
@app.route('/index')
def index():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('index.html')


# ✅ Protect Other Routes
@app.before_request
def require_login():
    allowed_routes = ['login', 'register', 'static', 'register_page']
    if request.endpoint not in allowed_routes and 'user' not in session:
        return redirect(url_for('login'))
    
@app.route('/about')
def about():
    # Render the HTML interface
    return render_template('about.html')
@app.route('/contact')
def contact():
    # Render the HTML interface
    return render_template('contact.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory('uploads', filename)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('upload.html', error="No file part in the request.")

        file = request.files['file']
        if file.filename == '':
            return render_template('upload.html', error="No file selected.")

        if file and allowed_file(file.filename):
            # Save the file with a timestamp to avoid overwrites
            filename = secure_filename(file.filename)
            filename = f"{int(time.time())}_{filename}"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            try:
                # Call the external function to analyze the image
                result = analyse.analyze_image(filepath)

                # Save the result and user details to JSON file
                user_details = {
                    "filename": filename,
                    "result": result
                }
                with open('user_data.json', 'a') as json_file:
                    json.dump(user_details, json_file)
                    json_file.write('\n')

                # Return the analysis result
                return render_template('upload.html', result=result, filename=filename)

            except Exception as e:
                # Handle errors in image analysis
                return render_template('upload.html', error=f"Error during analysis: {str(e)}")

        return render_template('upload.html', error="File type not allowed. Only PNG, JPG, and JPEG are supported.")

    return render_template('upload.html')

@app.route('/generate_report', methods=['GET', 'POST'])
def generate_report():
    if request.method == 'POST':
        # Ensure a file is uploaded
        if 'file' not in request.files:
            error_msg = "No file part in the request."
            app.logger.error(error_msg)
            return render_template('report.html', error=error_msg)

        file = request.files['file']
        if file.filename == '':
            error_msg = "No file selected."
            app.logger.error(error_msg)
            return render_template('report.html', error=error_msg)

        if file and allowed_file(file.filename):
            # Save the file with a timestamp to avoid overwrites
            filename = secure_filename(file.filename)
            filename = f"{int(time.time())}_{filename}"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            try:
                # Analyze the image
                result = analyse.analyze_image_report(filepath)
                if not result:
                    error_msg = "Failed to analyze the image."
                    app.logger.error(error_msg)
                    return render_template('report.html', error=error_msg)

                # Generate the report
                report_path = create_report_4(filepath, result, filename)
                if not report_path:
                    error_msg = "Failed to generate the report."
                    app.logger.error(error_msg)
                    return render_template('report.html', error=error_msg)

                # Fix the report URL to match the route
                report_filename = os.path.basename(report_path)  # Only get the filename, not the full path
                report_url = f"/report/{report_filename}"  # Correct URL path

                return render_template('report.html', result=result, report_url=report_url, filename=filename)

            except Exception as e:
                error_msg = f"Error during report generation: {str(e)}"
                app.logger.error(error_msg)
                return render_template('report.html', error=error_msg)

        error_msg = "File type not allowed. Only PNG, JPG, and JPEG are supported."
        app.logger.error(error_msg)
        return render_template('report.html', error=error_msg)

    return render_template('report.html')





from flask import send_from_directory

@app.route('/report/<filename>')
def download_report(filename):
    try:
        # Adjust the directory path as needed (e.g., 'reports/' or wherever the reports are saved)
        return send_from_directory('reports', filename, as_attachment=True)
    except FileNotFoundError:
        return "File not found", 404



@app.route('/start_scan', methods=['GET'])
def start_scan():
    global scan_thread
    if scan_thread is None or not scan_thread.is_alive():
        plastic_detection.stop_event.clear()
        scan_thread = Thread(target=plastic_detection.detect_plastic)
        scan_thread.start()
        return jsonify({"status": "Scanning started."})
    return jsonify({"status": "Scan already in progress."})

@app.route('/stop_scan', methods=['GET'])
def stop_scan():
    global scan_thread
    if scan_thread and scan_thread.is_alive():
        plastic_detection.stop_detection()
        scan_thread.join()
        return jsonify({"status": "Scanning stopped."})
    return jsonify({"status": "No scan in progress."})

if __name__ == '__main__':
    # Use the port provided by Render, or default to 5000
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
