#coding: utf-8

numero = int(input("Digite um número: "))
i = 0

while (i <= 10):
  total = numero * i
  print("{} x {} = {}").format(numero, i, total)
  i += 1
