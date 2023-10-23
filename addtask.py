
from todoist_api_python.api import TodoistAPI
api = TodoistAPI(API)

def send_task(birthdayBoy):
    try:
        task = api.add_task(
            content=("It's " + birthdayBoy + "'s birthday, go say something 🎂"),
            due_string="today"
        )
    except Exception as error:
        print(error)