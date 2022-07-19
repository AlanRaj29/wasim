##class student:
##    def __init__(self,m1,m2):
##        self.m1 = m1
##        self.m2 = m2
##    def sum(self,a,b):
##        s = a+b
##        return s
##
##s1 = student(59,69)
##print(s1.sum(5,9))

#METHOD OVERRIDDING:
    
##class a:
##    def show(self):
##        print("in a")
##class b(a):
##    def show(self):
##        print("in b")
##a1 = b()
##a1.show()


#LIST:

list=[]
a = int(input("Enter the list:"))
for i in range(1,a+1):
    b = int(input(f"Enter {i} index:"))
    list.append(b)
print(list)    
c = b
c.remove(max(c))
print(max(c))
