class animal:
    colour='white'
    def sleep(self):
          print('sleep...zzzz')

class dog(animal):
    def dogsound(self):
        print('boom boom   ')

class cat(animal):
    def catsound(self):
        print('mew mew  !')

class puppydog(dog):
    def puppysound(self):
        print('art art..!')



objpup= puppydog()
print(objpup.colour)#white
objpup.sleep()#sleep...zzzz
objpup.dogsound()#boom boom
objpup.puppysound()#art art..!


# print('==dog object')
# objdog=dog()
# print(objdog.colour)#white
# objdog.sleep()#sleep...zzzz
# objdog.dogsound()#boom boom
#
#
# print('==cat object')
# objcat = cat()
# print(objcat.colour)#white
# objcat.sleep()#sleep...zzzz
# objcat.catsound()#mew mew  !


#how many object oriented concept.explain them in details


