#  Take input number from User and check its a EVEN NUMBER or ODD Number

input_num = int(input("Please enter your first Number : -  "))

if(input_num<0):
    print('this is a NEGATIVE number')
elif(input_num%2==0):
    print(input_num,'is even number')
elif (input_num % 2 != 0):
    print(input_num, 'is odd number')
else:
    print(input_num,'is an invalid number')
