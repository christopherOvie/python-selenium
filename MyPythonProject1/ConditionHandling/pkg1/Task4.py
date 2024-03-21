

+num1 = int(input('pls enter num1 as  : '))
num2 = int(input('pls enter num2 as  : '))
num3 = int(input('pls enter num3 as  : '))

if(num1==num2==num3):
    print('equilatarl')
elif((num1==num2)or(num1==num3)or (num2==num3)):
    print('it is isosceless')