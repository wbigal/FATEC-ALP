#coding: utf-8

numero = -1

while(numero != 0):
  numero = int(input("Digite um número inteiro (zero para sair): "))
  if (numero > 0):
    print("{} é positivo").format(numero)
  elif (numero < 0):
    print("{} é negativo").format(numero)
