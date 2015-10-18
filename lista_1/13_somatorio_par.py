#coding: utf-8

maximo = 0
total = 0
i = 2

while (maximo < 100):
  maximo = int(input("Valor máximo (igual ou maior que 100): "))

while (i < maximo):
  total += i
  i += 2

print("Total dos pares entre 1 e {} é {}").format(maximo, total)
