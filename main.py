# Madlibs game

adjective1 = input("Enter an adjective (description): ")
noun1 = input("Enter an noun (person, place, thing): ")
adjective2 = input("Enter an adjective (description): ")
verb1 = input("Enter a verb ending with 'ing': ")
adjective3 = input("Enter an adjective (description): ")


print(f"Today I wnet to a {adjective1} zoo.")
print(f"In an exhibit, I saw a {noun1}.")
print(f"{noun1} was {adjective2} and {verb1}.")
print(f" I was {adjective3}!")

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