num=int(input("enter a number="))
for rows in range(num,0,-1): # for only pyramid range(0,num,+1)
      for cols in range (0,num-rows):
        print(end=" ")
      for cols in range (0,rows):
        print("*",end=" ")
      print()    




 #rows = 5,4,3,2,1
 #cols =0,01,012,0123,
