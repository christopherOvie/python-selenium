class parent:
       parentclassmethod=10
       print('am a parent class method')

class child(parent):
    childclassvariable=20

    def childclassmethod(self):
        print('am a child class method')



objchild=child()
#objchild.parentclassmethod()
objchild.childclassmethod()


