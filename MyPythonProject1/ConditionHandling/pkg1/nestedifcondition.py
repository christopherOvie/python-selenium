#take input from user check even or odd
# -ve display it is negative number
#  +ve  check number is even or odd


data = int(input('pls enter your number  :'))
if(data <0):
    print(data,'is a neative number')
else:
    if(data % 2==0):
        print(data,'is even number')
    else:
        print('odd number')