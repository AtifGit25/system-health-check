import psutil
import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

# Load environment variables from .env file
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

# Function to monitor top 20 running services
def monitor_services():
    try:
        services = []
        for proc in psutil.process_iter(['pid', 'name']):
            services.append(proc.info['name'])
            if len(services) >= 20:  # Limit to top 20 services
                break
        return f"Top 20 Running Services:\n{', '.join(services)}"
    except Exception as e:
        return f"Error monitoring services: {e}"

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

# Function to display the menu
def display_menu():
    print("\nSystem Health Check Tool")
    print("1. Check Disk Usage")
    print("2. Check Memory Usage")
    print("3. Check CPU Usage")
    print("4. Monitor Top 20 Running Services")
    print("5. Send Email Report")
    print("6. Exit")

# Main function
def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            print(check_disk())
        elif choice == '2':
            print(check_memory())
        elif choice == '3':
            print(check_cpu())
        elif choice == '4':
            print(monitor_services())
        elif choice == '5':
            receiver = input("Enter recipient's email: ")
            report = "\n".join([
                check_disk(),
                check_memory(),
                check_cpu(),
                monitor_services(),
                f"Report generated at: {time.ctime()}"
            ])
            send_email(receiver, report)
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the script
if __name__ == "__main__":
    import time
    try:
        main()
    except KeyboardInterrupt:
        print("\nScript stopped by the user.")
    except Exception as e:
        print(f"An error occurred: {e}")