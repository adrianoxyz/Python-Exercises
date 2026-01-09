# 06 - Faça um programa que leia três números e mostre o maior deles:

n1 = float(input("Digite o número 1: "))
n2 = float(input("Digite o número 2: "))
n3 = float(input("Digite o número 3: "))

if n1 > n2 and n1 > n2:
    print(f"O maior número é o {n1}")

elif n2 > n1 and n2 > n3:
    print(f"O maior número é o {n2}")

elif n3 > n1 and n3 > n1:
    print(f"O maior número é o {n3}")

else:
    print("Números iguais!")