
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

b = weight
result = round(b / height ** 2)
if result < 18.5:
    print("Your BMI is," +str(result)+ " you are underweight")
elif result >= 18.5 and result < 25:
    print("Your BMI is," +str(result)+ " you are a normal weight")
elif result >= 25 and result < 30:
    print("Your BMI is," +str(result)+ " you are slightly weight")
elif result >= 30 and result < 35:
    print("Your BMI is," +str(result)+ " you are obese")
else:
    print("Your BMI is," +str(result)+ " you are clinically obese")
