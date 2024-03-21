class animal:
      #property variable
   colour='white'

      #behaviour and  and function
   def sleep(self):
       print(" I am animal and I can sleep !")

# How to create the object of a class  


print(type(animal))
a1=animal()
a1.colour='brown'
print(a1.colour)
a1.sleep()

a2=animal()
a2.colour='black'
print(a2.colour)
a2.sleep()
