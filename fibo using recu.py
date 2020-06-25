def fibo(n):
    if (n<=1):
        return n
    else:
        n1=fibo(n-1)
        n2=fibo(n-2)
        n=n1+n2
        return n
n=int(input("enter the number of terms:"))
for i in range(n):
    print (fibo(i))
