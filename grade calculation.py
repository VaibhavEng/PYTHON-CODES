a=int(input("enter a subject 1 marks:"))
b=int(input("enter a subject 2 marks:"))
c=int(input("enter a subject 3 marks:"))
d=int(input("enter a subject 4 marks:"))
e=int(input("enter a subject 5 marks:"))
avg=(a+b+c+d+e)//5
print(avg)
if avg>90:
    print("passed with first class")
elif avg>70 and avg<90:
    print("passed with second class")
elif avg>35 and avg <70:
    print("passed with third class")
else:
    print("fail try again")
    


