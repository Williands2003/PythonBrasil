# Create a program that asks how much you earn per hour and the number of hours worked in the month. Calculate and display your total salary for that month.
# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.


hourly_wage = float(input("Enter your hourly wage: "))
hours_worked = float(input("Enter the number of hours you worked in the month: "))


salary = hourly_wage * hours_worked

print(f"Your salary for the month is ${salary:.2f}.")
