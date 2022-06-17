##try:
##  f = open("demofile.txt", "w")
##  try:
##    f.write("Lorum Ipsum")
##  except:
##    print("Something went wrong when writing to the file")
##  finally:
##    f.close()
##except FileNotFoundError:
##  print("File not found")
##except:
##    print("Something went wrong")

##a=int(input("enter the age"))
##if (a<=0):
##    raise Exception("not valid")
##elif (a>=18):
##    print("eligible for vote")
##else:
##    print("not eligible for vote")
