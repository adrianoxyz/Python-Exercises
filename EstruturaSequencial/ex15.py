# Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.

# Obs.: Salário Bruto - Descontos = Salário Líquido.

valorHora = float(input('Quanto ganha por hora? '))
horaMes = float(input('Quantas horas trabalha por mês? '))
salarioBruto = valorHora * horaMes

descontoImpostoDeRenda = salarioBruto * 0.11
descontoInss = salarioBruto * 0.08
descontoSindicato = salarioBruto * 0.05

descontoTotal = (descontoImpostoDeRenda + descontoInss + descontoSindicato)
salarioLiquido = (salarioBruto - descontoTotal)


print(f'O valor do salário bruto é: {salarioBruto}')
print(f'O valor do salário liquído é: {salarioLiquido}')