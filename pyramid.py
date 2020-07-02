n=int(input("enter a number n:"))
for rows in range(0,n):
    for cols in range (0,n-rows-1):
        print(end=" ")
    for cols in range (0,rows+1):
        print("*",end=" ")
    print()    
        
