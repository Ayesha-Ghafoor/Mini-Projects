# BMI Calculator using function with parameters

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)

    # Determine health status
    if bmi < 18.5:
        status = "Underweight"
    elif 18.5 <= bmi < 24.9:
        status = "Normal weight"
    elif 25 <= bmi < 29.9:
        status = "Overweight"
    else:
        status = "Obese"

    return bmi, status


# Take input from user
try:
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    bmi, status = calculate_bmi(weight, height)

    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"Health Status: {status}")
except ValueError:
    print("Please enter valid numbers for weight and height.")
