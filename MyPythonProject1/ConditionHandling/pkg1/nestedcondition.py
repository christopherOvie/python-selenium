#take input from user check even or odd
# -ve display it is negative number
#  +ve  check number is even or odd


data = int(input('pls enter your number  :'))
if(data >=0):
    print(data,'is a positive number')
    if(data %2==0):
        print(data,'is an even number')
    else:
        if(data%2==1):
            print(data,'is odd number')
else:
         print('does not exist')


