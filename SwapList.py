#SWAPLIST:
#1

a = [12,35,9,56,24]

def swap(a):
    a[0],a[4] = a[4],a[0]
    return a
print(swap(a))

#2

a = [1,2,3]

def list(a):
    a[0],a[2] = a[2],a[0]
    return a
print(list(a))    

#3

a = [23,65,19,90]

def element(a):
    a[0],a[2] = a[2],a[0]
    return a
print(element(a))

#4

a = [1,2,3,4,5,6,7]

def pos(a):
    a[1],a[4] = a[4],a[1]
    return a
print(pos(a))


#COUNT()

#1

a = [15,6,7,10,12,20,10,28,10]
b = a.count(10)
print(b)


#2

a = [8,6,8,10,8,20,10,8,8]
b = a.count(16)
print(b)









