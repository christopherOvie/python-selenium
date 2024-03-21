# Take first input Number from User
num1= int(input("Please enter your first Number : -  "))

# # Take second  input Number from User
# num2= int(input("Please enter your second  Number : -  "))

if(num1%5==0 and num1%11==0):
    print('Number is Divisible by both 5 and 11')
elif((num1)%5):
    print('Number is Divisible by both 5 only')
elif ((num1) % 11):
        print('Number is Divisible by both 11 only')
else:
    print('Number is Not Divisible by 5 and 11 both')
