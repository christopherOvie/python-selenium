class animal:
#property , variable
    color="white"

#behaviour-method and function
    def sleep(self):
        print(" I am animal and I can sleep !")



# How to create the object of a class

print(type(animal))

a1=animal()
a1.color="Brown"
print(a1.color)
a1.sleep()

a2=animal()
a2.color="black"
print(a2.color)
a2.sleep()