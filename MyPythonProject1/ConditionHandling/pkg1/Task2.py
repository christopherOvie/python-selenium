data = int(input('pls enter num1 as  : '))
if(data<0):
    print('invalid value')
elif(data==0):
    print('zero')
else:
    if(data>0):
        print('even or odd')
if(data%2==0):
       print(data ,' is even ')
if (data%2 ==1):
    print(data, ' is odd ')