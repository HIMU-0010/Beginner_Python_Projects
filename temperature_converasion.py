unit = input("Is the temperture to be converted is in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter your temperature: "))

if unit == "C" or unit =="c":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp}F")
elif unit == "F" or unit =="f":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celsius is: {temp}C")
else:
    print(f"{unit} is not a valid unit of Temperature")