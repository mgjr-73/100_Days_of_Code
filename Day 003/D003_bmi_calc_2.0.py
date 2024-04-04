height = input("height (m): ")
weight = input("weight (kg): ")

bmi = int(weight) / float(height) ** 2

if bmi < 18.5:
    print(f"Your BMI is {bmi}. You are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}. You are within normal range.")
elif bmi < 30:
    print(f"Your BMI is {bmi}. You are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}. You are obese.")
else:
    print(f"Your BMI is {bmi}. You are clinically obese.")