# System Resource Monitor &amp; Alerting Dashboard

A full-stack system monitoring tool built with Python that tracks CPU, Memory, and Disk usage in real-time. It features a web dashboard for visualization, historical data logging via SQLite, and automated email alerts when system thresholds are exceeded.

# Features

Real-time Monitoring: Captures system metrics every few seconds using `psutil`.

Automated Alerts: Sends email notifications via SMTP (Gmail) when resources exceed safety thresholds.

Data Persistence: Logs all metrics to a local SQLite database for historical analysis.

Web Dashboard: Flask-based interface to visualize system health trends.

Security: Uses environment variables (`.env`) to secure sensitive credentials.

# Tech Stack

*Language: Python 3.x*
Backend: Flask, SQLite
System Interface: psutil
Notifications: smtplib (Email)
Frontend: HTML/CSS, Jinja2 Templating

# Installation & Setup

1.  Clone the repository:
    ```bash
    git clone https://github.com/yourusername/sys-monitor.git
    cd sys-monitor
    ```

2.  Install Dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3.  Run the Monitor (Background Service):
    ```bash
    python monitor.py
    ```

4.  Run the Dashboard (Web UI):
    ```bash
    python app.py
    ```
    Access the dashboard at `http://127.0.0.1:5000`
