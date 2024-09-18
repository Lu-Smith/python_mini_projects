# Converting a weight

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (Kg or Lbs): ").strip().lower()

if unit == "kg":
    weight = weight * 2.205
    unit = "lbs"
    print(f"Your weight is: {round(weight, 1)} {unit}.")
elif unit == "lbs":
    weight = weight / 2.205
    unit = "kg"
    print(f"Your weight is: {round(weight, 1)}{unit}.")
else:
    print(f"{unit} is not valid .Enter the valid unit (Kg or Lbs)")