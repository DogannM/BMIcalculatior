x = input("Enter your weight in kg : ")
y = input("Enter your height in cm : ")
x = float(x)
y = float(y)
bmi = x / y ** 2
print("Your BMI is : ", bmi)

if bmi < 18.5:
    print("You're Underweight")
elif 18.5 <= bmi <= 25:
    print("You're Normal")
elif 25 < bmi <= 30:
    print("You're Overweight")
else:
    print("You're Obese")
    