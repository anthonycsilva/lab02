
def maximoMinimo():
#essa função calcula o  maximo e o minimo de numeros pré determinados

    return max(3, 2.8, 3.9), min(7,2,4,1,0)

def calculaMedia(a,b,c):
#essa  função calcula a média de 3 numeros inteiros
#int, int, int -> float
    return (a+b+c)/3

def  diferencaMedia(a,b,c):
#essa função seleciona o maior numero dos 3 e subtrai da média
#int, int, int -> float
    return max(a,b,c) - calculaMedia(a,b,c)

def  somaMedia(a,b,c):
#essa função seleciona o menor numero  dos 3 e soma com a média
#int, int, int -> float
    return min(a,b,c) + calculaMedia(a,b,c)

