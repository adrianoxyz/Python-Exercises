# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

temperaturaF = float(input('Digite a temperatura em farenheit:\n '))
temperaturaC = 5 * ((temperaturaF - 32) / 9)
print(f"A temperatura {temperaturaF} convertida para Celsius é igual á: {temperaturaC:.2f}")