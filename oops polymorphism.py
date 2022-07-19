#Polymorphism

class India():
     def capital(self):
       print("New Delhi")
 
     def language(self):
       print("Hindi and English")
 
class USA():
     def capital(self):
       print("Washington, D.C.")
 
     def language(self):
       print("English")
 
obj1 = India()
obj2 = USA()
obj1.capital()
obj1.language()
obj2.capital()
obj2.language()
