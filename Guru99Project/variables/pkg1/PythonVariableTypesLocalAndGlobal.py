# Declare a variable and initialize it
f = 101
print (f)

# Global vs. local variables in functions
def someFunction():
    f ='i am learning python'
    print(f)
someFunction()
print(f)