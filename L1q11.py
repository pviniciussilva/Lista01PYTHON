'''Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:
   °o pruduto do dobro de primeiro com metade do segundo.
   °a soma do triplo do primeiro com o terceiro.
   °o terceiro elevado ao cubo.'''

#entrada
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o sengundo número: '))
n3 = float(input('Digite o terceiro número: '))

#processamento
opdpms = n1 ** 2 + n2 / 2
astp = n1 * 3 + n3
otc = n3 ** 3

#saída
print('O pruduto do dobro de primeiro com metade do segundo {:.0f}'.format(opdpms))
print('A soma do triplo do primeiro com o terceiro é {:.0f}'.format(astp))
print('O terceiro elevado ao cubo é {:.0f}'.format(otc))