num=int(input("Enter a number:"))
print("The multiplication table of;num")
if num<=0:
        for i in range(13,-1,-1):
            print(num,"x",i,"=",num*i)
else:    
    for i in range(0,13):
            print(num,"x",i,"=",num*i)
        
   