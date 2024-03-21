class A:          ##multilevel inheritance
    def m1(self):
        print('this is m1 method from class A')

class B(A):
    def m2(self):
        print('this is m2 method from class B')

class C(B):
    def m3(self):
        print('this is m3 method from class C')


aobj=A()
aobj.m1()  #this is m1 method from class A


bobj=B()
bobj.m1()  #this is m1 method from class A
bobj.m2()  #this is m2 method from class b

c= C()
c.m1() #this is m1 method from class A
c.m2()#this is m2 method from class B
c.m3()#this is m3 method from class C