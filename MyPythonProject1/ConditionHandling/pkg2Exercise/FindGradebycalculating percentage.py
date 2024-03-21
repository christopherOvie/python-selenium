# Take input from User
math =int(input("Please enter math marks : -   "))
english =int(input("Please enter english marks : - "))
physics =int(input("Please enter physics marks : - "))
chemistry =  int(input("Please enter chemistry marks : - "))
biology =int(input("Please enter biology marks : - "))

average=(math+english+physics+chemistry+biology)/5

if(average>=90):
    print('Your grade is  --  A')
elif(average>=80 and average<90):
    print('Your grade is  --  B')
elif (average >= 60 and average < 80):
    print('Your grade is  --  C')
elif (average >= 40 and average < 60):
    print('Your grade is  --  D')
elif (average < 40):
    print('Your grade is  --  D')
else:
    print('NO GRADE')
