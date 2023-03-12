'''Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:
   °o pruduto do dobro de primeiro com metade do segundo.
   °a soma do triplo do primeiro com o terceiro.
   °o terceiro elevado ao cubo.'''

#entrada
numero_1 = float(input('Digite o primeiro número: '))
numero_2 = float(input('Digite o sengundo número: '))
numero_3 = float(input('Digite o terceiro número: '))

#processamento
calculo_1 = numero_1 ** 2 + numero_2 / 2
calculo_2 = numero_1 * 3 + numero_3
calculo_3 = numero_3 ** 3

#saída
print('O pruduto do dobro de primeiro com metade do segundo {:.0f}'.format(calculo_1))
print('A soma do triplo do primeiro com o terceiro é {:.0f}'.format(calculo_2))
print('O terceiro elevado ao cubo é {:.0f}'.format(calculo_3))