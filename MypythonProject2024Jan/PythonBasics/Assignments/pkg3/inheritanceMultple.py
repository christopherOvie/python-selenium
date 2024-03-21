class Man:
    def working(self):
        print('the man is working')

class  Woman:
    def cooking(self):
        print('the woman is cooking')


class boy(Man,Woman):
    def school(self):
        print('boy is going t school')


objboy=boy()
objboy.working()  #the man is working
objboy.cooking()   #the woman is cooking
objboy.school()  #boy is going t school
w= Woman()
w.cooking()  #the woman is cooking

