#1 INTERCHANGE LIST ELEMENTS
##a =[1,2,3]
##def list(a):
##    a[0],a[-1]=a[-1],a[0]
##    return a
##print(list(a))   


#2SWAP TWO ELEMENTS IN LIST

list = []
a=int(input("Enter the list number:"))
for i in range(1,a+1):
      b=int(input(f"Enter {i} index:"))
      list.append(b)
print(list)
pos1=int(input("Enter the pos1:"))
pos2=int(input("Enter the pos2:"))
def swap(list, pos1, pos2): 
       
    list[pos1], list[pos2] = list[pos2], list[pos1] 
    return list
   
print(swap(list, pos1-1, pos2-1)) 
