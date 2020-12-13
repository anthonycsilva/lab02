def calculaPA(a,r,n):
#essa função calcula o valor do ultimo termo da P.A, dado o primeiro termo, a razão e a quantidade de termos
#int, int, int -> int

    return a + (n-1)*r

def calculaTermos(a, u, r):
#Essa função calcula  o total de termos da PA dado o primeiro termo, o ultimo, e a razão
#int, int, int -> int
    return (-a + r + u)/r

