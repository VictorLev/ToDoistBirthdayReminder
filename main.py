from datetime import date
from addtask import send_task
from ListofBirthdays import BirthdayDictionary  

#Test Commit
 
def main():

    today = date.today()
    TheDate = today.strftime('%m-%d')
    if TheDate in BirthdayDictionary['Birthdates'] :
        index = BirthdayDictionary['Birthdates'].index(TheDate)
        send_task(BirthdayDictionary['name'][index])

if __name__ == "__main__":
    main()