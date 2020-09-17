student_name=set()
while True:
    print("""select a option form the below menu:
1.Inserting one name
2.Inserting multiple names
3.Updating an exisiting name
4.deleting a name
5.view all the names
6.quit the program""")
    ch = int(input("enter your choice:"))
    if ch==1:
        #pass means nothing / there will a coming soon
##        pass
        student_name.add(input("enter student name:"))
    elif ch == 2:
        names = input("enter multiple names comma seprated:")
        names = names.strip()
        if not names == "" or not names is None or not names == " ":
            student_name.update(names.split(","))
    elif ch == 3:
        ch1 = int(input("How would like to input data \n1.name \n2.number"))
        if ch1==1:
            name = input("enter the name you want to modify:")
            if name in student_name:
                student_name[student_name.index(name)]= input("enter name:")
            else:
                print("this name is not available")
        else:
            for i in range(len(student_name)):
                print("{}. {}".format(i+1, student_name[i]))
            idx = int(input("the number of the name u want to change:"))
            if idx <= len(student_name):
                student_name[idx-1]= input("enter name:")
            else:
                print("invalid input")
    elif ch == 5:
        for name in student_name:
            print(name)
    elif ch == 6:
        print("""Thank you for using our program!""")
        break
    else:
        print("you have entered a wrong choice. please try again.")
