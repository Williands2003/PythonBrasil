# English: Make a Program that asks for the temperature in degrees Fahrenheit, transforms and displays the temperature in degrees Celsius.
#PT: Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

# Get the temperature in Fahrenheit from the user
fahrenheit = float(input("Enter the temperature in Fahrenheit: "))

# Convert the temperature to Celsius
celsius = 5 * ((fahrenheit - 32) / 9)

print(f"The temperature in Celsius is {celsius:.2f}.")
