# Take input month Number from User
input_num = int(input("Please enter your first Number : -  "))

if(input_num%2==0):
    print(input_num,'is even')
elif(input_num  % 2 !=0):
    print(input_num, 'is odd')
else:
    print(input_num, 'is invalid')

