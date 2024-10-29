height = float(input("Enter your height"))

weight = float(input("Enter your weight"))


bmi : float = (weight) / (height**2)

print(f"Your BMI is {bmi:.2f}")
if bmi ==18.5 :
    print("You are under weight")
elif bmi > 25 :
    print("You are normal")
elif bmi > 30 :
    print("You are over weight")
elif bmi > 35 :
    print("You are obese")
else:
    print("You are clinically obesed")
        
