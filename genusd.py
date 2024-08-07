import os
import django
from datetime import datetime, timedelta
import random

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'digidet.settings')
django.setup()

from tracker.models import User,UserData

# Define constants
user_id = User.objects.get(id=2)
APPS = ['Microsft Edge', 'Mozilla Firefox', 'PowerPoint']
DAYS = 21

# Generate and insert data
start_date = datetime.now().date() - timedelta(days=DAYS)

for day in range(0,21,2):
    date = start_date + timedelta(days=day)
    for app in APPS:
        timespent = random.randint(600, 1200)  # Time spent between 30 seconds and 1 hour
        userdata = UserData(uid=user_id, appname=app, timespent=timespent, ondate=date)
        userdata.save()

print(f"Inserted data for the past {DAYS} days.")
