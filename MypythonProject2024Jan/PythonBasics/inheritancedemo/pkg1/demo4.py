class mother:
     def cooking(self):
         print('my mother cooks food')

class father:
    def purchaseGrossary(self):
        print('my father bringd grossary')




class child(mother,father) :
      def school(self):
          print('i go to school everyday')


objchild=child()
objchild.cooking()#my mother cooks food
objchild.purchaseGrossary()#my father bringd grossary
objchild.school()  #i go to school everyday
