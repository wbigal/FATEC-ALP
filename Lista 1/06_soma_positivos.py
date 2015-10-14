#coding: utf-8

n = int(input("Digite um número inteiro: "))
total = 0.0
i = 0

while i < n:
  valor = float(input("Digite um número real positivo: "))
  if (valor > 0):
    total += valor
  i += 1

print("Total: {}").format(total)
