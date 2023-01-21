diametro = int(input()) 
a, l, p = map(int,input().split()) #recebendo entrada de três valores inteiros na mesma linha
if diametro<=a and diametro<=l and diametro<=p: #comparação com área, lado e perímetro
  print("S")
else:
  print("N")
