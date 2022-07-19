a = [2,3,4,5,7]
b = [2,4,11,5,12]
def list(a,b):
    r = []
    for i in a:
        for i in b:
            r.append(i)
print(r)            

#COMMON LIST:            
##a = [2,3,4,5,7]
##b = [2,4,11,5,12]
##def cl(a,b):
##    a = set(a)
##    b = set(b)
##    if (a & b):
##        print(a & b)
##    else:
##        print("no common list")
##cl(a,b)       

##a = [2,3,4,5,7]
##b = [2,4,11,5,12]
##def c_l(a,b):
##    return list(set(a) & set(b))
##print(c_l(a,b))

##a = [2,3,4,5,7]
##b = [2,4,11,5,12]
##c = [element for i in a if i in b]
##print(c)
