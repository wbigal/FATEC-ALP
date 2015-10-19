#coding: utf-8

vet_a = []
vet_b = []
vet = []

i = 0

while (i < 10):
  vet_a.append(int(input("Digite um valor: ")))
  i += 1

i = 0

while (i < 10):
  vet_b.append(int(input("Digite um valor: ")))
  i += 1

i = 0

while (i < 20):
  if (i < 10):
    vet.append(vet_a[i])
  else:
    vet.append(vet_b[i - 10])
  i += 1

i = 0

while (i < 20):
  print(vet[i])
  i += 1
