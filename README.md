# Email Automation Tool 📧

A command-line email automation tool that sends personalized emails to multiple contacts from a CSV file, built with Python.

## Features
- Sends personalized emails to multiple recipients at once
- Reads contacts from a CSV file
- Works with Gmail using App Passwords
- Simple and easy to customize

## How to Use

1. Add your contacts to email.csv in this format:

name,email
John Doe,johndoe@example.com
Jane Smith,janesmith@example.com

2. Open email_automation.py and replace the placeholders:

sender = "YOUR_EMAIL@gmail.com"
password = "YOUR_APP_PASSWORD"

3. Run the script:

python email_automation.py

## How to Get a Gmail App Password
1. Go to your Google Account settings
2. Navigate to Security
3. Enable 2-Step Verification if not already enabled
4. Search for App Passwords
5. Generate a new app password and paste it into the script

## Files
- email_automation.py - main script
- email.csv - contacts file with name and email columns

## Requirements
- Python 3.x
- No external libraries needed
