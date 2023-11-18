import psutil
import time

def monitor_cpu(threshold):
    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)

            print(f"Current CPU Usage: {cpu_usage}%")

            if cpu_usage > threshold:
                print(f"Alert! CPU usage exceeds {threshold}%.")

            time.sleep(1)

    except KeyboardInterrupt:
        print("\nMonitoring stopped by the user.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Set the predefined threshold 80%
    threshold = 80

    monitor_cpu(threshold)