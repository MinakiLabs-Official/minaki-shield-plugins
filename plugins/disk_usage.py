# plugins/disk_usage.py
import psutil

def detect(line):
    try:
        disk_usage = psutil.disk_usage('/')
        threshold = 20  # Alert if less than 20% free space
        if disk_usage.percent > (100 - threshold):
            return True
    except Exception as e:
        print(f"Error in disk_usage plugin: {e}")
    return False
