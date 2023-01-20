# Problema 1827 - Beecrowd - Iniciante - Nível 1

while True: #repetir até a entrada ser verdadeira
    try:
        n = int(input()) #entrada
        condicao1 = n//3 #condiçao para o 1

        for i in range(0,n):
            linha = '' #para definir que aqui será linha
            for j in range(0,n):
                nmatriz = 0 #numeros que aparecerao
                if i == j: 
                    nmatriz = 2 #perceba que 
                if n-j-1 == i:
                    nmatriz = 3
                if i>= condicao1 and i<=n-1-n//3 and j>= condicao1 and j<= n-1-condicao1:
                    if i == n//2 and j == n//2:
                        nmatriz = 4
                    else:
                        nmatriz = 1

                linha+=str(nmatriz) #concatenação

            print(linha)

        print()
