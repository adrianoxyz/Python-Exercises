# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a - o produto do dobro do primeiro com metade do segundo .
# b - a soma do triplo do primeiro com o terceiro.
# c - o terceiro elevado ao cubo.

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo numero: '))
num3 = float(input('Digite o terceiro numero: '))

a = (num1 * num1) * (num2 / 2)
b = (num1 * 3) + num3
c = num3 ** 3

print("o produto do dobro do primeiro com metade do segundo = ", a)
print("a soma do triplo do primeiro com o terceiro = ", b)
print("o terceiro elevado ao cubo = ", c)