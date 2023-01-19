#criar função com as variáveis dadas pelo problema:

def solve(d,vf,vg):

  #usar pitágoras para medir a distancia:
    h = (144+d*d)**(1/2)
    tguardac = h/vg #tempo da guardac
    tfugit = 12/vf #tempo do fugitivo
    
    #caso em que a guarda costeira não alcança, pois o tempo é maior
    if tguardac > tfugit:
        ans = 'N'
    else:
    #caso em que a guarda costeira alcança
        ans = 'S'
    return ans

#criar o loop para as entradas
while True:
    try:
        a,b,c = (int(x) for x in input().split())
        ans = solve(a,b,c)
        print(ans)
#definir EOFerror, não há mais input para ser lido
    except EOFError:
        break
