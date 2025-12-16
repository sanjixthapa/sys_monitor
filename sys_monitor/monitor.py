# monitor.py
import psutil
import time
import smtplib
from email.mime.text import MIMEText
from config import *
import database

# Initialize Database
database.init_db()


def send_alert(subject, body):
    if not EMAIL_ENABLED:
        print(f"[ALERT SIMULATION] {subject}: {body}")
        return

    try:
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECEIVER_EMAIL

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        print(f"Email sent: {subject}")
    except Exception as e:
        print(f"Failed to send email: {e}")


def check_thresholds(cpu, mem, disk):
    alerts = []
    if cpu > CPU_THRESHOLD:
        alerts.append(f"High CPU Usage: {cpu}%")
    if mem > MEMORY_THRESHOLD:
        alerts.append(f"High Memory Usage: {mem}%")
    if disk > DISK_THRESHOLD:
        alerts.append(f"Low Disk Space: {disk}% used")

    if alerts:
        send_alert("System Alert", "\n".join(alerts))


def monitor_system():
    print("Starting System Monitor...")
    try:
        while True:
            # Collect Metrics
            cpu = psutil.cpu_percent(interval=1)  # Blocking call for 1 sec
            mem = psutil.virtual_memory().percent
            disk = psutil.disk_usage('/').percent

            # Log to DB
            database.log_metrics(cpu, mem, disk)
            print(f"Logged: CPU {cpu}% | Mem {mem}% | Disk {disk}%")

            # Check Alerts
            check_thresholds(cpu, mem, disk)

            # Wait before next check (interval=1 already waits 1 sec)
            time.sleep(4)
    except KeyboardInterrupt:
        print("\nStopping monitor.")


if __name__ == "__main__":
    monitor_system()