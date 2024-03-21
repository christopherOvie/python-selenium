# Take input from User - First side length of Triangle
first_side= int(input("Please enter length of first side : -   "))

# Take input from User - Second side length of Triangle
Second_side= int(input("Please enter length of Second side : -   "))

# Take input from User - Second side length of Triangle
Third_side= int(input("Please enter length of Third side : -   "))

if(first_side!=Second_side and first_side!=Third_side):
    print('This triangle is a SCALENE Triangl')

elif(first_side==Second_side and first_side==Third_side):
    print('This triangle is a EQUILATERAL Triangle')

elif(first_side==Second_side or first_side==Third_side):
    print("This triangle is a ISOSCELES Triangle")