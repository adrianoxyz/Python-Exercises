# João, um pescador, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
# Imprima os dados do programa com as mensagens adequadas.

pesoPeixe = float(input('Quantos KG tem o peixe?'))
excessoPesoPeixe = pesoPeixe - 50
valorMulta = excessoPesoPeixe * 4
print(f'O peso do peixe é: {pesoPeixe}')
print(f'O excesso do peso do peixe é: {excessoPesoPeixe}')
print(f'O valor da multa é: {valorMulta}')