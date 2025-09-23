# Vulnerable Flask Web Application

⚠️ **WARNING: This application contains intentional security vulnerabilities for educational and testing purposes. DO NOT use in production!**

## Purpose
This is a deliberately vulnerable Flask web application designed for:
- Security testing with tools like OWASP ZAProxy
- Educational purposes to demonstrate common web vulnerabilities
- Penetration testing practice

## Quick Start
```bash
pip install flask
python app.py
```

Then visit: http://localhost:5001

## Included Vulnerabilities

### 1. SQL Injection (Login Form)
- **Location**: `/login` endpoint
- **Issue**: String concatenation in SQL query
- **Test**: Try username `admin'--` or `' OR '1'='1`

### 2. Cross-Site Scripting (XSS)
- **Location**: `/search` endpoint  
- **Issue**: User input displayed without escaping
- **Test**: Search for `<script>alert('XSS')</script>`

### 3. Missing Authentication
- **Location**: `/profile` endpoint
- **Issue**: Direct URL access without proper auth check
- **Test**: Visit `/profile?user_id=1` without logging in

### 4. Unrestricted File Upload
- **Location**: `/upload` endpoint
- **Issue**: No file type or size validation
- **Test**: Upload executable files or files with malicious names

### 5. Missing Security Headers
- **Location**: All responses
- **Issue**: No X-Frame-Options, CSP, etc.
- **Test**: Check response headers with browser dev tools

## Test Accounts
- admin / admin123
- user1 / password  
- test / test

## Application Features
- Basic login/logout
- User registration
- User profiles
- Search functionality
- File upload

## ZAProxy Testing
This app is perfect for automated security scanning with OWASP ZAProxy. All vulnerabilities should be easily detectable by the scanner.