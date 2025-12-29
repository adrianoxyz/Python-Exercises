# Faça um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:

# F - Feminino
# M - Masculino
# Sexo Inválido.

letra = input('Digite a letra referente ao sexo:\n ')

if letra.upper() == 'F':
    print('Sexo Feminino!')

elif letra.upper() == 'M':
    print('Sexo Masculino!')

else:
    print('Sexo inválido!')