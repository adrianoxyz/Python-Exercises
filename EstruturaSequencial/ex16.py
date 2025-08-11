# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros 
# quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros 
# quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

metrosQuadrados = float(input("Digite o tamanho em metros quadrados a ser pintado: "))
QtdTinta = metrosQuadrados / 3
lataDeTinta = 18
valorLataDeTinta = 80
qtdLataDeTintas = 18 / QtdTinta
precoTotal = qtdLataDeTintas * valorLataDeTinta
print(f"O valor total a ser gasto com tinta é: {precoTotal:.2f}")
