from datetime import timedelta,date
from addtask import send_task
from ListofBirthdays import BirthdayDictionary  

def main():
    today = date.today()+ timedelta(days=1)
    TheDate = today.strftime('%m-%d')
    for index, Birthdate in enumerate(BirthdayDictionary[1]):
        if TheDate == Birthdate:
            send_task(BirthdayDictionary[0][index])
            print('its '+ BirthdayDictionary[0][index]+ ' Birthday')
    
if __name__ == "__main__":
    main()