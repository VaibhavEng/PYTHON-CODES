def menu():
    print("1.check if number is perfect or not")
    print("2.find the factorial of the number")
    print("3.print the n number of fibonnaci series")
    select=int(input("enter choice:"))
    if select==1:
        check(int(input("enter the input:")))    
    elif select==2:
        factorial(int(input("enter the number:"))) 
    elif select==3:
        fibonaci(int(input("enter the number range: ")))
    else:
        print("incorrect option")
              
def check(n):
    s=0
    for i in range(1,n):
        if(n%i==0):
            s=s+i
    if(s==n):
        print("perfect no")
    else:
        print("is not perfect no")
   
def  factorial(n):
    
    facto=1
    if n<0:
        print("factorial no avi")
    elif n==0:
        print("factorial=1")
    else:
        for i in range(1,n+1):
            facto=facto*i
        print(facto)
        
def fibonaci(n):
    
    x,y=1,0
    while y<n:
        print(y)
        x,y=y,x+y
                
    
menu ()
#check(int(input("enter the input:")))
#factorial(int(input("enter the number:")))
#fibonaci(int(input("enter the number range: ")))
    
     

        
      
