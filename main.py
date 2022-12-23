from datetime import date
from addtask import send_task
from ListofBirthdays import BirthdayDictionary  

#test git ignore
 
def main():

    today = date.today()
    TheDate = today.strftime('%m-%d')
    if TheDate in BirthdayDictionary[1] :
        index = BirthdayDictionary[1].index(TheDate)
        send_task(BirthdayDictionary['name'][index])

if __name__ == "__main__":
    main()