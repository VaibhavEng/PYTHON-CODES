n=int(input("enter number of rows="))

for i in range(0,n):
    v=1
    for j in range(1,n-i):
        print("  ",end="")
    for k in range (0,i+1):
        print("  ",v,end="")
        v=int(v*((i-k)/(k+1)))
    print()    
    
    
        
##k=0
##i=2
##add=1
##add=int(add*((i-k)/(k+1)))
##print(add)

