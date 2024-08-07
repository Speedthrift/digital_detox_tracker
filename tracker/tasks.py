# your_app/tasks.py
from celery import shared_task
import time

@shared_task
def your_task():
    # print("Task is running every second.")
    # Add your script logic here
    with open('C:\\Users\\arnav\\Unused\\Documents\\output.txt', 'a') as f:
        f.write("Task is running every second.\n")
'''
celery -A digidet worker --loglevel=info
celery -A digidet beat --loglevel=info
'''