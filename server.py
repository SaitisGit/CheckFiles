import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

# Define your email and password for sending emails
sender_email = "youremail@gmail.com"
sender_password = "yourpassword"
recipient_email = "recipients_email@gmail.com"

# Define the source folder to search for files
source_folder = "Y:\\"

# Define the file extensions to search for
file_extensions = [".doc", ".ppt", ".pptx", ".xls", ".xlsx"]

# Initialize an empty list to store the file paths
file_paths = []

# Function to search for files with specified extensions
def search_files(folder, extensions):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if any(file.lower().endswith(ext) for ext in extensions):
                file_paths.append(os.path.join(root, file))

# Search for files with specified extensions
search_files(source_folder, file_extensions)

# Step 1: Create a text file to save the file paths
text_file_path = "file_paths.txt"

# Step 2: Write the file paths to the text file using UTF-8 encoding
with open(text_file_path, "w", encoding="utf-8") as text_file:
    for file_path in file_paths:
        text_file.write(file_path + "\n")

# Step 3: Read the content of the text file
with open(text_file_path, "r", encoding="utf-8") as text_file:
    file_paths_content = text_file.read()

# Set up the email server
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, sender_password)

# Create the email message with the text file attachment
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = "Found Files"

# Step 4: Attach the text file to the email
attachment = MIMEText(file_paths_content)
attachment.add_header('Content-Disposition', 'attachment', filename='file_paths.txt')
msg.attach(attachment)

# Send the email
server.sendmail(sender_email, recipient_email, msg.as_string())

# Quit the email server
server.quit()
