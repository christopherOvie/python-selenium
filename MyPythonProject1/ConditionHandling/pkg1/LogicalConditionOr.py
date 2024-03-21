#take number from user check number is >100 this is invalid
#if number is bet 0 and -100 invalid

marks = int(input('pls enter marks as  : '))

#check if condition fpor >100 and <0

if(marks > 100 or marks<0):
    print(marks,'is invalid')

else:
    print(marks,'is valid')