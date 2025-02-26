import psutil

def check_disk_usage():
    disk_usage = psutil.disk_usage('/')
    return f"Disk Usage: {disk_usage.percent}%"

def main():
    print("System Health Check Tool")
    print(check_disk_usage())

if __name__ == "__main__":
    main()