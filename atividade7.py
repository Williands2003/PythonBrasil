# English Write a program that calculates the area of ​​a square, then shows twice this area to the user.
# PT Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.


side = float(input("Enter the length of the side of the square: "))


area = side ** 2

# Calculate the double of the area
double_area = 2 * area

print(f"The double of the area of the square with side {side} is {double_area}.")
