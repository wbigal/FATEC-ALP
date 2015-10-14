#coding: utf-8

n = int(input("Digite um número inteiro: "))
total = 0.0
i = 0

while i < n:
  total += float(input("Digite um número real: "))
  i += 1

print("Total: {}").format(total)
