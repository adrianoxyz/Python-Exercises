# Exercício 13
# Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para Megabytes e Kilobytes, usando as seguintes fórmulas:

# Para Megabytes: Gigabytes * 1024
# Para Kilobytes: Gigabytes * 1024 * 1024
# Responda o tamanho do arquivo em Megabytes e o tamanho em Kilobytes.

entradaGB = float(input('Digite o tamanho em GB: '))
conversorMB = entradaGB * 1024
conversorKB = (entradaGB * 1024 * 1024)

print (f'O valor informado convertido em MB, é igual a: {conversorMB:.2f}' )
print (f'O valor informado convertido em KN, é igual a: {conversorKB:.2f}' )