#take  3 number from user

num1 = int(input('pls enter num1 as  : '))
num2 = int(input('pls enter num2 as  : '))
num3 = int(input('pls enter num3 as  : '))
if(num1>num2 and num1>num3):
    print(num1,'is greatest')
elif (num2 > num1 and num2 > num3):
        print(num2, 'is greatest')
elif (num3 > num1 and num3> num2):
    print(num3, 'is greatest')