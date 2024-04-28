#PT Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

#English Write a Program that asks for the radius of a circle, calculates and displays its area.

import math

radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2

print("The area of the circle is", round( area, 2))
