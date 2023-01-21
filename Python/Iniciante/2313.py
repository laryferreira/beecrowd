a,b,c = map(int, input().split()) #entrada com split para receber os três valores separados

def maior(a,b,c): #encontrar o maior entre os três valores para ser utilizado como hipotenusa
    if a>=b and a>=c: # a = hipotenusa
        hip= a**2
        ls = b**2 + c**2
        if hip == ls: #para ser retângulo, deve cumprir pitágoras (hipotenusa ao quadrado = soma dos catetos ao quadrado)
            print('Retangulo: S')
        else:
            print('Retangulo: N')

    elif b>=a and b>=c: # b = hipotenusa
        hip = b**2
        ls = a**2 + c**2
        if hip==ls:
            print('Retangulo: S')
        else:
            print('Retangulo: N')
    
    elif c>=a and c>=b: # c = hipotenusa
        hip = c**2
        ls = b**2 + a**2
        if hip==ls:
            print('Retangulo: S')
        else:
            print('Retangulo: N')
        
    

if a + b <= c or a + c<= b or c + b <= a: #triangulo só é válido se a soma dos lados for maior do que o terceiro lado, aqui estão as excessões
    print('Invalido')    

elif a==b and a==c and b==c: #tres lados com valores iguais
    print('Valido-Equilatero')
    maior(a,b,c)
    
elif b==c or a==c or a==b: #é um caso isolado do equilátero, dois lados com valores iguais
    print('Valido-Isoceles')
    maior(a,b,c)

elif a!=b and a!=c and b!=c: #tres lados com valores distintos
    print('Valido-Escaleno')
    maior(a,b,c)
