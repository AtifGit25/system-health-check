import psutil
import smtplib
from email.mime.text import MIMEText
import time
import os
from dotenv import load_dotenv

# Load email credentials from .env file
load_dotenv()

# Function to check disk usage
def check_disk():
    try:
        disk = psutil.disk_usage('/')
        return f"Disk Usage: {disk.percent}%"
    except Exception as e:
        return f"Error checking disk: {e}"

# Function to check memory usage
def check_memory():
    try:
        memory = psutil.virtual_memory()
        return f"Memory Usage: {memory.percent}%"
    except Exception as e:
        return f"Error checking memory: {e}"

# Function to check CPU usage
def check_cpu():
    try:
        cpu = psutil.cpu_percent(interval=1)
        return f"CPU Usage: {cpu}%"
    except Exception as e:
        return f"Error checking CPU: {e}"

# Function to send email
def send_email(receiver, report):
    try:
        sender = os.getenv("EMAIL_ADDRESS")  # From .env file
        password = os.getenv("EMAIL_PASSWORD")  # From .env file

        # Create the email
        msg = MIMEText(report)
        msg["From"] = sender
        msg["To"] = receiver
        msg["Subject"] = "System Health Report"

        # Send the email
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender, password)
            server.sendmail(sender, receiver, msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Main function
def main():
    receiver = input("Enter recipient's email: ")  # Ask for email
    interval = 4 * 60 * 60  # 4 hours in seconds

    while True:
        print("Checking system health...")

        # Perform health checks
        disk = check_disk()
        memory = check_memory()
        cpu = check_cpu()

        # Create the report
        report = f"""
        System Health Report:
        {disk}
        {memory}
        {cpu}
        Report generated at: {time.ctime()}
        """

        # Print and send the report
        print(report)
        send_email(receiver, report)

        # Wait for the next check
        print(f"Next check in {interval // 3600} hours...")
        time.sleep(interval)

# Run the script
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Script stopped by the user.")
    except Exception as e:
        print(f"An error occurred: {e}")