# Take input month Number from User
month_number= int(input("Please enter your first Number : -  "))

if(month_number >0 and month_number<=12):
    if(month_number==2):
        print('Total number of days are : - 28 or 29')
    elif(month_number==1 or month_number==3 or month_number==5 or month_number ==7 or month_number==8
      or month_number==10  or month_number==12):
        print('Total number of days are : - 31')
    elif (month_number == 1 or month_number == 4 or month_number == 6 or month_number == 9 or month_number == 11):
        print('Total number of days are : - 30')


else:
    print("Your month number is INVALID, Please enter correct month number")