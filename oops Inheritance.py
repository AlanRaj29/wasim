#Single Inheritance:
 #In single inheritance child class is derived from only one parent class.

##class parent:
##    def func1(Brand):
##        print("HP")
##class child(parent):
##    def func2(Brand):
##        print("Dell")
##object = child()
##object.func1()
##object.func2()


#Multiple Inheritance:
 #In multiple inheritance a class can be derived from more than one base class.

##class mother:
##    
##    def mother(name):
##        print(name.mothername)
##        
##class father:
##    
##    def father(name):
##        print(name.fathername)
##        
##class Son(mother,father):
##    def parents(name):
##        print("mother:",name.mothername)
##        print("father:",name.fathername)
##s = Son()
##s.mothername = "b"
##s.fathername = "a"
##s.parents()
    
#Multilevel Inheritance:

##class Grandfather:
## 
##    def __init__(self, grandfathername):
##        self.grandfathername = grandfathername
## 
##
##class Father(Grandfather):
##    def __init__(self, fathername, grandfathername):
##        self.fathername = fathername
##        Grandfather.__init__(self, grandfathername)
## 
##class Son(Father):
##    def __init__(self,sonname, fathername, grandfathername):
##        self.sonname = sonname
##        Father.__init__(self, fathername, grandfathername)
## 
##    def name(self):
##        print("Son name :", self.sonname)
##        print("Father name :", self.fathername)
##        print('Grandfather name :', self.grandfathername)
##       
##s1 = Son("me","You","Your father")
##print(s1.grandfathername)
##s1.name()


#Hierarchical Inheritance:

##class parent:
##    def func1(name):
##        print("Father name :","wasim")
##        
##class child1(parent):
##    def func2(name):
##        print("Frist wife :","priya")
##        
##class child2(parent):
##    def func3(name):
##        print("Second wife :","vidya")
##h1 = child1()
##h2 = child2()
##h1.func1()
##h1.func2()
##h2.func3()

#Hybride Inheritance

class clg:
    def func1(me):
        print("clg fun")
        
class clg1(clg):
    def func2(me):
        print("clg fun 1")
        

class clg2(clg):
    def func3(me):
        print("clg fun 2")


class clg3(clg1,clg2,clg):
    def func4(me):
        print("clg fun 3")

h = clg3()
h.func1()
h.func2()
h.func3()
h.func4()        
                
            
    












