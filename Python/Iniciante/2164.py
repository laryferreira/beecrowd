n = int(input()) #entrada

if n==1 or n==2: #outputs definidos por fibonacci
    print(1.0)

else:
    fibpt1 = ((1 + 5**0.5)/2)**n #separação da operação em duas partes para facilitar revisão de código
    fibpt2 = ((1 - 5**0.5)/2)**n
    fibtotal = (fibpt1 - fibpt2) / (5**0.5) #junção da operação
    
    print(f'{fibtotal:.1f}') #print com 1 casa após a vírgula
