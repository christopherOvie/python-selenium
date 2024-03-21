# Declare a variable and initialize it
f = 101
print(f)
# Global vs. local variables in functions
def someFnction():
#global f
    f= "i am learning python"
    print(f)  #i am learning python
someFnction()
print(f)  #101