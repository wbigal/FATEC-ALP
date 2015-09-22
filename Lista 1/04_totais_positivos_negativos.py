#coding: utf-8

numero = -1
positivo = 0
negativo = 0

while(numero != 0):
  numero = int(input("Digite um número inteiro (zero para sair): "))
  if (numero > 0):
    print("{} é positivo").format(numero)
    positivo += numero
  elif (numero < 0):
    print("{} é negativo").format(numero)
    negativo += numero

print("Total dos positivos: {}").format(positivo)
print("Ttoal dos negativos: {}").format(negativo)
