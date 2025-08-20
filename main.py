import math

#2 - Escreva um programa que calcula a área do círculo, recebendo o raio como entrada.

raio = float(input ("Digite o raio: "))
area = math.pi * raio ** 2

print (f"{area:.2f}")