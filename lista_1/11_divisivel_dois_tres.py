#coding: utf-8

numero = -1

while (numero != 0):
  numero = int(input("Digite um número: "))
  if (numero % 2 == 0):
    print("{} é divisível por 2").format(numero)
  elif (numero % 3 == 0):
    print("{} é divisível por 3").format(numero)
