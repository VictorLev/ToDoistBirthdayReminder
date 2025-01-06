import os
import json

from todoist_api_python.api import TodoistAPI
from datetime import datetime

# Initialize Todoist API
API = os.getenv("TODOIST_API_KEY")
api = TodoistAPI(API)

birthday_data = json.loads(os.getenv("BIRTHDAY_DATA"))

# Function to send task
def send_task(birthdayBoy):
    try:
        task = api.add_task(
            content=f"It's {birthdayBoy}'s birthday, go say something 🎂",
            due_string="today"
        )
        print(f"Task created for {birthdayBoy}")
    except Exception as error:
        print(f"Error creating task for {birthdayBoy}: {error}")

# Get today's date
today = datetime.now().strftime("%m-%d")

# Check birthdays and send tasks
for name, birthday in birthday_data.items():
    if birthday == today:
        send_task(name)