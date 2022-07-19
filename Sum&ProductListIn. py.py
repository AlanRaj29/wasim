##a=[12,14,28,104,2]
##b = a
##l = str(b)
##sum = 0
##for i in l:
####    key = i%10
##    sum+=int(b)
##    b//=10
##    if(key!=0):
##        product*=key
##    else:
##        pass
##print(sum)
##print(product)    
    
    
##a=[12,14,28,104,2]
##l = str(a)
##r = []
##for i in a: 
##    sum = 0
##    for j in str(i):
##        sum+=int(j)
##    r.append(sum)
##print("a =",a)    
##print("value of sum",r)
##r = []
##for i in a:
##    product = 1
##    for j in str(i):
##        product*=int(j)
##    r.append(product)    
##print("value of product",r)
##
##



##a=[12,14,28,104,2]
##def list(a):
##    product = 1
##    for i in a:
##        product = product*i
##    return product
##print(list(a))
##




##product=0
##for i in a:
##    product+=i
##print(product)    
##

##n=[12,14,28,104,2]
##def multiply(n):
##    total = 1
##    for i in range(1, len(n)):
##        total *= n[i]
##    print(total)

    
##lst = [5, 20 ,15]
##product = []
##for i in lst:
##    product.append(i*5)
##print(product)


a=[12,14,15,108]
r=0



for i in a:
    print(i)
    sum=0
    product=1
    v=i
    while(v>0):
        lnum=v%10
        sum+=lnum
        if(lnum != 0):
            product*=lnum
        v//=10    
        print('sum',sum)
        print('product',product, "\n")    
    if(i%sum ==0 and i %product==0):
        print("divisible")
        r+=1

print(r)







