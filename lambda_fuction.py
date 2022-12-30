from datetime import datetime
import pytz
from addtask import send_task
from ListofBirthdays import BirthdayDictionary  

#test git ignore

def lambda_handler(event, context):

    MelTimeZone= pytz.timezone('Australia/Melbourne')
    today = datetime.now(MelTimeZone)
    TheDate = today.strftime('%m-%d')
    for index, Birthdate in enumerate(BirthdayDictionary[1]):
        if TheDate == Birthdate:
            send_task(BirthdayDictionary[0][index])
            print('its '+ BirthdayDictionary[0][index]+ ' Birthday')
    
