from math import pi, pow
#Faça um Programa que peça o raio de um circulo, calcule e mostre sua área do circulo = pi * r ** 2
raio = float(input('Digite o valor do raio do circulo: '))
area = ( pi * pow( raio,2))
print('O valor da área do circulo é: {:.2f}'.format(area))