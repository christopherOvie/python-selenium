#take input from user
#check number if number is even print  this is negative
#check if number is zero   it is zero
#check if positive check even or odd

data=int(input('please enter the number   '))

if(data < 0):
     print('this is negative number',data)
elif(data ==0):
    print('this is zero')
elif(data % 2 ==0):
    print(data, 'is a even number')
elif(data%2==1):
    print(data,'is odd number')