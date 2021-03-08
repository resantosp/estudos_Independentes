#Faça um programa que peça uma nota, entre zero e dez.
#Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido. 

n = int(input('Dê uma nota para o atendimento (0-10): '))
while n > 10:
    n = int(input('Entrada inválida. Por favor, dê uma nota de 0 a 10 para o atendimento: '))
print('Sua opinião é muito importante. Obrigada pela colaboração.')
