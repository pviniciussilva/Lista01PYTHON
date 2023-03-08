"""Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
    ◦ Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    ◦ comprar apenas latas de 18 litros;
    ◦ comprar apenas galões de 3,6 litros;
    ◦ misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias."""
import math
tamanho_area = float(input('Qual o tamanho da area? '))
galao = tamanho_area / 21.6
lata = tamanho_area /108
dez_porcento_de_folga = tamanho_area + (10/100 * tamanho_area)
numero_de_latas = math.floor(dez_porcento_de_folga / 108)
numero_de_galoes = dez_porcento_de_folga - 108 * numero_de_latas
quantidade_de_latas = math.ceil(2 / 21.6)
latas_galoes = quantidade_de_latas + numero_de_latas
#print(f'A area{tamanho_area} precisa de {math.ceil(tamanho_area/lata)} latas')
print('A quantodade de latas e galoes é: {}'.format(latas_galoes))