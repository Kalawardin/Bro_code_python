converter = input("Enter your dimension: (kg,lb)")
weight = float(input("Enter weight:"))

if converter == "kg":
    weight = weight * 2.20462
    print(f"Your weight is: {round(weight,3)} {converter}")
elif converter == "lb":
    weight = weight / 2.20462
    print(f"Your weight is: {round(weight,3)} {converter}")
else:
    print(f"{converter} was not a valid dimension.")
    


