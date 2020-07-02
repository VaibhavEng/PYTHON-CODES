h=float(input("enter a height in meter :"))
w=float(input("enter a weight in kg  :"))
(BMI)=w//(h**2)
print(float(BMI))
if (BMI)<18:
    print("underwight")
elif BMI>=18 and BMI<=22.5:
    print("normal")
elif BMI>22.5 and BMI<=25:
    print("overwight")
else:
    print("obese")

