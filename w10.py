x =  "a"
try :
    h = int(input("Please input a number:"))
    print("The number you want is ",h)
    print("Which type you want? Incremental(0) or  Less(1) ")
    t= int(input("Please input the 0 or 1:"))
 
    if  t == 0 :
        for i in range(1,h+1,1):
            print(x*i)
  
        for i in range(h-1,0,-1):
            print(x*i)
 
    if t == 1 :
        for i in range(h,0,-1):
            print(x*i)
        for i in range(2,h+1,1):
            print(x*i)
 
    if  t  !=0 and t  !=1 :
        print("You insert a wrong number")
except:
    print("You insert a wrong number")
    print ("Please run again")

# This is test 