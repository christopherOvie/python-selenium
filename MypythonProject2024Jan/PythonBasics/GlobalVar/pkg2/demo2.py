class Test1:

    # Special Method - constructer
    # Name of special method __init__
    # __init__ method will get Automatically called when an object of class is crated
    # This method will be used to initialize the instace variables  during the object creation
    def f1(self):
        print("I am in Normal Method !")

    def __init__(self, passi, psssj):
        print("I am predefined method I will Get called Automatically when object of class is created !")
        self.a = passi
        self.b = psssj
##explain init method and constructor in detail

def sum(self):
    print("sum is :", self.a + self.b)


def sub(self):
    print("sub is :", self.a - self.b)


t1 = Test1(100, 50)
t1.sum()
t1.sub()
t2 = Test1(60, 40)
t2.sum()
t2.sub()