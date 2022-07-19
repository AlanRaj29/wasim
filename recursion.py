#RECURSION:
#1

##count = 0
##
##def func():
##    global count
##    count+=1
##    print(count)
##    if(count==10):
##        pass
##    else:
##        func()
##    
##func()
##

#2

##n = int(input("Enter the num:"))
##def printNumber(n):
##  
##  if n > 0:
##       printNumber(n - 1)
##   
##       print(n, end = ' ')
##
##printNumber(n)

#3
##r = 10
##n = int(input("Enter the num:"))
##def printNumber(n,r):
##  
##  if n >= 0:
##       printNumber(r,(n - 1)-1)
##   
##       print(r,n, end = ' ')
##
##printNumber(r,n)



n = int(input("Enter the num:"))
def printNumber(n):
  
  if n < 0:
       printNumber(n + 1)
   
       print(n, end = ' ')

printNumber(n)



