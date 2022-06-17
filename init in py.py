#Constructor Function 
#Example 1

##class lap:
##    def __init__(self,color,company,ram):
##        self.color = color
##        self.company = company
##        self.ram = ram
##lp1 = lap("Artic Grey","Lenovo","4 + 4 GB")
##lp2 = lap("silver","Dell","8GB")
##print(lp1.ram)
##print(lp2.ram)

#Example 2
##class ac:
##    def __init__(Alan,name,ton,rating):
##        Alan.name = name
##        Alan.ton = ton
##        Alan.rating = rating
##ac1 = ac("vestar",1.5,3.2)
##ac2 = ac("Blue Star",2,5)
##print(ac1.name)
##print(ac2.rating)


class employee1():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
 
class childemployee(employee1):
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
       
emp1 = employee1('harshit',22,1000)
 
print(emp1.age)
