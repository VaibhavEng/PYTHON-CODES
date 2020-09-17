d={}
while True:
    print("""select a option from following
menu:
1.ADD A NEW DATE
2.UPDATE THE EXISITING VALUE
3.DELETE A VALUE
4.VIEW ALL THE VALUES""")
    ch = int(input("choose your choice:"))
    if ch==1:
        key=(input("enter the date to added:"))
        value=int(input("enter the corona cases:"))
        d.update({key:value})
        print(d)
    elif ch==2:
        key=input("enter the date you want to modify")
        
        if key in d:
            value=int(input("enter the updated corona cases:"))
            d.update(d.fromkeys([key],value))
        else:
            print("this date is not available")
    elif ch==3:
        key=input("enter the date you want to delete:")
        if key in d:
            del d[key]
        else:
            print("this date is not available")
                
    elif ch==4:
        for i in d.items():
            print(i)
    else:
        print("you have enterd a wrong choice. please try again")
            
                
