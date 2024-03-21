# Take First Number from User
num1 = int(input('Please enter First Number : - '))

# Take Second Number from User
num2 = int(input('Please enter second Number : - '))

# Take Second Number from User
num3 = int(input('Please enter third Number : - '))

if(num1>num2 and num1>num3):
    print('largest among three is',num1)

if(num2>num1 and num2>num3):
    print('largest among three is', num2)
if(num3>num1 and num3>num1):
    print('largest among three is', num3)