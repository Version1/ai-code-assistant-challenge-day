#!/usr/bin/env python3
"""
Vulnerable Flask Web Application for Security Testing
WARNING: This application contains intentional security vulnerabilities
for educational and testing purposes. DO NOT use in production!
"""

from flask import Flask, request, render_template, redirect, url_for, session, flash
import sqlite3
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'vulnerable_secret_key_123'  # VULNERABILITY: Weak secret key

# Database initialization
def init_db():
    conn = sqlite3.connect('vulnerable_app.db')
    cursor = conn.cursor()
    
    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT,
            email TEXT,
            full_name TEXT
        )
    ''')
    
    # Insert test users (passwords stored in plain text - VULNERABILITY)
    test_users = [
        ('admin', 'admin123', 'admin@example.com', 'Administrator'),
        ('user1', 'password', 'user1@example.com', 'John Doe'),
        ('test', 'test', 'test@example.com', 'Test User')
    ]
    
    for user in test_users:
        cursor.execute('INSERT OR IGNORE INTO users (username, password, email, full_name) VALUES (?, ?, ?, ?)', user)
    
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # VULNERABILITY 1: SQL Injection - using string concatenation
        conn = sqlite3.connect('vulnerable_app.db')
        cursor = conn.cursor()
        
        # Intentionally vulnerable SQL query
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        print(f"Executing query: {query}")  # Debug output
        
        try:
            cursor.execute(query)
            user = cursor.fetchone()
            
            if user:
                session['user_id'] = user[0]
                session['username'] = user[1]
                flash('Login successful!')
                return redirect(url_for('profile'))
            else:
                flash('Invalid credentials!')
        except Exception as e:
            flash(f'Database error: {str(e)}')
        
        conn.close()
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        full_name = request.form['full_name']
        
        conn = sqlite3.connect('vulnerable_app.db')
        cursor = conn.cursor()
        
        try:
            # Using parameterized query for registration (but not for login!)
            cursor.execute('INSERT INTO users (username, password, email, full_name) VALUES (?, ?, ?, ?)',
                         (username, password, email, full_name))
            conn.commit()
            flash('Registration successful! Please login.')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Username already exists!')
        
        conn.close()
    
    return render_template('register.html')

@app.route('/profile')
def profile():
    # VULNERABILITY 3: Missing authentication check
    # Anyone can access profiles by going to /profile?user_id=X
    user_id = request.args.get('user_id', session.get('user_id'))
    
    if not user_id:
        return redirect(url_for('login'))
    
    conn = sqlite3.connect('vulnerable_app.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    user = cursor.fetchone()
    conn.close()
    
    if user:
        return render_template('profile.html', user=user)
    else:
        flash('User not found!')
        return redirect(url_for('login'))

@app.route('/search')
def search():
    query = request.args.get('q', '')
    
    # VULNERABILITY 2: XSS - directly outputting user input without escaping
    if query:
        # Simulate search results
        results = [
            f"Result 1 for: {query}",
            f"Result 2 matching: {query}",
            f"Found item: {query}"
        ]
    else:
        results = []
    
    return render_template('search.html', query=query, results=results)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # VULNERABILITY 4: File upload with no validation
        if 'file' not in request.files:
            flash('No file selected')
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            flash('No file selected')
            return redirect(request.url)
        
        # No file validation - accepts any file type!
        upload_folder = 'uploads'
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
        
        # Using original filename without sanitization
        file.save(os.path.join(upload_folder, file.filename))
        flash(f'File {file.filename} uploaded successfully!')
    
    return render_template('upload.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully!')
    return redirect(url_for('login'))

# VULNERABILITY 5: Missing security headers
@app.after_request
def after_request(response):
    # Intentionally NOT setting security headers
    # Missing: X-Frame-Options, X-XSS-Protection, X-Content-Type-Options, etc.
    return response

if __name__ == '__main__':
    init_db()
    # VULNERABILITY: Debug mode enabled and running on all interfaces
    app.run(debug=True, host='0.0.0.0', port=5001)