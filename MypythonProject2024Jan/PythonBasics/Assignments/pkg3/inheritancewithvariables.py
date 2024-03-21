class A:
    x,y=10,20##multilevel inheritance
    def m1(self):
       # print('this is m1 method from class A',self.x+self.y)
        print(self.x+self.y)

class B(A):
    a,b=15,25
    def m2(self):
        print('this is m2 method from class B',self.a+self.b)

class C(B):
    i,j=1,2
    def m3(self):
        print('this is m3 method from class C',self.i+self.j)

        a=A()
        a.m1()

        c=C()
        c.m1()
        c.m2()
        c.m3()