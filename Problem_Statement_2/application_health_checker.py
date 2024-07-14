import requests
import time
import logging

APP_ENDPOINT = 'http://127.0.0.1:54010/greet'
uptime_start = None
total_uptime_seconds = 0
logging.basicConfig(filename='application_health_checker.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def check_application_health():
    global uptime_start, total_uptime_seconds
    try:
        response = requests.get(APP_ENDPOINT)
        if response.status_code == 200:
            logging.info(f'Application is UP - Status Code: {response.status_code}')
            if uptime_start is None:
                uptime_start = time.time()  # Start tracking uptime
        else:
            logging.warning(f'Application is DOWN - Status Code: {response.status_code}')
            if uptime_start is not None:
                uptime_seconds = time.time() - uptime_start
                total_uptime_seconds += uptime_seconds
                uptime_start = None

    except requests.exceptions.RequestException as e:
        logging.warning(f'Application is DOWN - Exception: {e}')
        if uptime_start is not None:
            uptime_seconds = time.time() - uptime_start
            total_uptime_seconds += uptime_seconds
            uptime_start = None

def format_uptime(seconds):
    days, remainder = divmod(seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{int(days)} days, {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds"

if __name__ == "__main__":
    try:
        while True:
            check_application_health()
            if uptime_start is not None:
                current_uptime_seconds = total_uptime_seconds + (time.time() - uptime_start)
            else:
                current_uptime_seconds = total_uptime_seconds
            logging.info(f"Current uptime: {format_uptime(current_uptime_seconds)}")
            time.sleep(10)
    except KeyboardInterrupt:
        if uptime_start is not None:
            uptime_seconds = time.time() - uptime_start
            total_uptime_seconds += uptime_seconds
        logging.info(f"\nFinal total uptime: {format_uptime(total_uptime_seconds)}")
        print("Health check stopped by user.")
