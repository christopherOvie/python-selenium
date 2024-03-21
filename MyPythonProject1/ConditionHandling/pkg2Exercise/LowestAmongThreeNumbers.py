# Take First Number from User
num1 = int(input('Please enter First Number : - '))

# Take Second Number from User
num2 = int(input('Please enter second Number : - '))

# Take Second Number from User
num3 = int(input('Please enter third Number : - '))


if(num1<num2 and num1<num3):
    print(num1,'smallest among three numbers')
if (num2 < num1 and num2 < num3):
        print(num2, 'smallest among three numbers')
if (num3 < num1 and num3 < num2):
            print(num3, 'smallest among three numbers')
