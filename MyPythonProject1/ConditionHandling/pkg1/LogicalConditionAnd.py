#take number from user check number is >100 this is invalid
#if number is +ve and multiple of 2 print even numbrr
#if number is -ve and multiple of 2 print odd numbrr
num = int(input('pls enter marks as  : '))

#check if condition fpor >100 and <0

if((num >= 0) and (num % 2==0)):
    print(num, 'is even ')

elif((num >=0) and (num % 2==1)):
    print(num,'is positive odd number')
else:
    print(num,'is invalid')