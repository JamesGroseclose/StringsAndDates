# James Groseclose CIS 261
#  Strings and Dates

sample_date = input("Enter date: ")

while sample_date != '-1':
    tokens = sample_date.split()
    month = tokens[0]
    if month == 'January':
        month_num = 1
    elif month == 'February':
        month_num = 2
    elif month == 'March':
        month_num = 3
    elif month == 'April':
        month_num = 4
    elif month == 'May':
        month_num = 5
    elif month == 'June':
        month_num = 6
    elif month == 'July':
        month_num = 7
    elif month == 'August':
        month_num = 8
    elif month == 'September':
        month_num = 9
    elif month == 'October':
        month_num = 10
    elif month == 'November':
        month_num = 11
    elif month == 'December':
        month_num = 12
    else:
        month_num = 0
    if len(tokens) >= 3 and month_num != 0 :
        date_adjusted = tokens[1]
        if date_adjusted[len(date_adjusted) -1] == ',':
            date_adjusted = date_adjusted[0:len(date_adjusted) -1]
            year = tokens[2]
            print(str(month_num)+'/'+date_adjusted+'/'+str(year))
        else:
            print("Date entered is not valid")
    else:
        print("Date entered is not valid")
    sample_date = input("Enter date: ")

