#coding: utf-8

numero = int(input("Digite um número inteiro: "))

if (numero % 2 == 0):
  print("{} é par.").format(numero)
else:
  print("{} é impar.").format(numero)
