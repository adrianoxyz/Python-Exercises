# 12 - Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

h = float(input('Digite sua altura: '))
sexo = input('Digite seu sexo:\n M - Masculino\n F - Feminino\n')

if sexo == 'M':
    pesoIdeal = (72.7 * h) - 58
    print(f'Seu peso ideal é:  {pesoIdeal:.2f}')
elif sexo == 'F':
    pesoIdeal = (62.1 * h) - 44.7
    print(f'Seu peso ideal é:  {pesoIdeal:.2f}')
else:
    print('Sexo informado não é válido!')