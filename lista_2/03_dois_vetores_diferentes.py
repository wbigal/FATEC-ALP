#coding: utf-8
from random import randint

A = []
B = []
R = []
i = 0
tamA = int(input("Tamanho do vetor A: "))
tamB = int(input("Tamanho do vetor B: "))

print("Vetor A")
while(i < tamA):
  A.append(randint(0,100))
  print(A[i])
  i += 1

print("Vetor B")
i = 0
while(i < tamB):
  B.append(randint(0,100))
  print(B[i])
  i += 1

i = 0
while(i < (tamA + tamB)):
  if (i < tamA):
    R.append(A[i])
  else:
    R.append(B[i - tamA])
  i += 1

print("Vetor R")
i = 0
while(i < (tamA + tamB)):
  print(R[i])
  i += 1
