#Replace string elements in a list using if...else method

##a = ["i","am","raj"]
##for i in range(len(a)):
##    if a[i]=="raj":
##        a[i]="me"
##print(a)        

#Caps the first letter

a = input("enter a para to capitilize => ")

alphacaps=("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
alphasmall=("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
for i in range(len(alphasmall)):
    if(alphasmall[i]==a[0]):
       a = alphacaps[i] + a[1:]

print(a)
