import psutil
import logging
import time

logging.basicConfig(filename='system_health_monitoring.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

CPU_THRESHOLD = 10.0
MEMORY_THRESHOLD = 40.0
DISK_THRESHOLD = 10.0
TARGET_PROCESS = "pycharm"

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f'CPU usage is high: {cpu_usage}%')

def check_memory_usage():
    memory_usage = psutil.virtual_memory().percent
    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f'Memory usage is high: {memory_usage}%')

def check_disk_usage():
    disk_usage = psutil.disk_usage('/').percent
    if disk_usage > DISK_THRESHOLD:
        logging.warning(f'Disk usage is high: {disk_usage}%')

def check_running_processes():
    for proc in psutil.process_iter(['pid', 'name']):
        if TARGET_PROCESS.lower() in proc.info['name'].lower():
            logging.info(f'Process {TARGET_PROCESS} is running with PID: {proc.info["pid"]}')

if __name__ == "__main__":
    try:
        while True:
            check_cpu_usage()
            check_memory_usage()
            check_disk_usage()
            check_running_processes()
            time.sleep(60)
    except KeyboardInterrupt:
        logging.info("Monitoring stopped by user.")
