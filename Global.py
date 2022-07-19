a = 104
sum = 0
product = 1
b = a
while(b>0):
    rum = b%10
    sum+=rum
    b//=10
    if(rum!=0):
        product*=rum
    else:
        pass
print(sum)
print(product)

if(a%sum==0):
    print(1)
else:
    print(0)





##a = 10
##b = a
##l = str(b)
##sum = 0
##for i in range(l):
##    sum+=int(a)
##    


