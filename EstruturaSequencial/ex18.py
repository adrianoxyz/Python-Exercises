# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanhoDoArquivo = float(input('Qual o tamanho do arquivo em MB:\n '))
velocidadeDaInternet = float(input('Qual a velocidade da internet em MB:\n '))

tempoDeDownload = tamanhoDoArquivo / velocidadeDaInternet

print(f"O tempo de download em minutos é: {tempoDeDownload:.2f} minutos")