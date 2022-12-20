
from todoist_api_python.api import TodoistAPI
api = TodoistAPI("2e6152d14a83c3791e9f3ea1225abfdd3b095764")

def send_task(birthdayBoy):
    try:
        task = api.add_task(
            content=("It's " + birthdayBoy + "'s birthday, go say something 🎂"),
            due_string="today"
        )
    except Exception as error:
        print(error)