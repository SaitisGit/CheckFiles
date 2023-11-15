# File Search and Email Script

## Overview

This Python script searches for files with specific extensions in a specified folder and sends the file paths in an email attachment. It uses the smtplib library for email functionality and the concurrent.futures library for parallel file searching.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python: [https://www.python.org/](https://www.python.org/)

Install required Python packages:

```bash
pip install tqdm

## Configuration
Open the script (file_search_and_email.py) and set the following variables:

python

sender_email = "your_email@example.com"
sender_password = "your_email_password"
recipient_email = "recipient_email@example.com"
source_folder = "path/to/source/folder"
file_extensions = [".doc", ".ppt", ".pptx", ".xls", ".xlsx"]
Replace the placeholder values with your actual email credentials and the desired source folder and file extensions.

## Usage
Run the script using the following command:

bash

python server.py
The script will perform the following steps:

1. Search for Files
It will search for files in the specified folder with the specified extensions.

2. Save File Paths
It will save the file paths to a text file (file_paths.txt) in the same directory.

3. Send Email
It will send an email to the specified recipient with the file paths attached.

## Customization
Feel free to customize the script according to your needs:

Modify the email subject, body, or recipients in the script.
Adjust the file extensions, search folder, or any other parameters based on your requirements.

## Notes
This script is for educational purposes only. Use it responsibly and be aware of email provider policies regarding automated email sending.
