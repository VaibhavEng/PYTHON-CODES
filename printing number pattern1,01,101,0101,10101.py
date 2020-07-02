n=int(input("enter a the number of rows:"))
for row in range(0,n+1):
    for cols in range(1,row+1):
        if((row+cols)%2!=0):
            print("0",end="")
        else:
            print("1",end="")
    print()
    
        
    
    
