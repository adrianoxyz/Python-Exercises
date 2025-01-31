# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valorSalarioHora = float(input('Digite o valor do seu salário por hora: '))
horasTrabalhadas = float(input('Digite a quantidade de horas trabalhadas no mês: '))

salarioMensal = valorSalarioHora * horasTrabalhadas
print('O valor do salário é: ', salarioMensal)