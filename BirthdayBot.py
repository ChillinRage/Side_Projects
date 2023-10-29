import smtplib
import pandas
import datetime

my_email   = 'REDACTED'
main_email = 'REDACTED'
passw      = 'REDACTED'

namelist = r"path to birthday list in excel/csv"
dateLog  = r"path to history log"

# connector = smtplib.SMTP('smtp.gmail.com')
# connector.starttls()  # secure connection
# connector.login(email, passw)
# connector.sendmail(from, to, 'Subject:TEST\n\ntest body')
# connector.close()
#=====================================================================================================
def add_person(name, date, email): # add person to birthday list
    with open(namelist,'a') as file:
        file.write(f'\n{name},{date},{email}')

def todate(): # return today's date
    day = datetime.date.today()
    return '/'.join( str(day).split('-')[::-1] )

def birthday_email(data): # return info of today's bday person
    curDay, curMonth = map(int, today[:-5].split('/'))
    
    for person in data['name'].to_list():
        info = data[data['name'] == person]
        day, month = map(int, info['DOB'].values[0][:-5].split('/'))
        if (day == curDay) and (month == curMonth):
            return info.values[0].tolist()

    return None

def postfix(n): # add postfix to birthday years
    ones = n % 10
    if 1 <= ones <= 3:
        return str(n) + [0,'st','nd','rd'][ones]
    return str(n) + 'th'

def check_run(): # prevent repeated sends in a day
    lastday = open(dateLog,'r').read()
    if today == lastday:
        quit()
    else:
        open(dateLog,'w').write(today)
        open(dateLog,'r').close()
        
#===========================================================================================================
def check_bday():
    global today
    today = todate()
    check_run()
    bday_list = pandas.read_csv(namelist)
    bday_info = birthday_email(bday_list)
    
    if bday_info:
        name, age, email = bday_info
        age = postfix( int(today[-4:]) - int(age[-4:]) )

        subject = 'Happy Birthday!'
        msg1 = f'Today marks your {age} birthday.'
        msg2 = "Regardless of how bright or dark yesterday has been, rejoice in this special day of the year, " \
               "go out with friends or family, spend time by yourself. As long as you've fun is all that matters."
        msg3 = "Beep Beep Boop Boop. This is a birthday wish sent from someone who got your info from a national " \
               "data breach. Do not panic. Do not fret. I am not coming for you."
        msg4 = 'Sike! The name of the person can be found in the email address. Have a great Birthday! '

        connector = smtplib.SMTP('smtp.gmail.com', 587)
        connector.starttls()
        connector.login(my_email,passw)
        connector.sendmail(my_email, email, f'Subject:{subject}\n\n{msg1}\n{msg2}\n\n\n\n{msg3}\n\n\n{msg4}{name}')
        connector.sendmail(my_email,main_email,f"Subject:Notice of Birthday\n\nToday is {name}'s birthday.")
        connector.close()

        print("NOTICE: Today is {}'s birthday!".format(name))
        input() # ONLY CLOSE WHEN I'VE ACKNOWLEDGED.
    quit()

check_bday()
#add_person('name','date','email')
