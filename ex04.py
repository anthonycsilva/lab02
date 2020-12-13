import math

def calcularHipotenusa(b,c):
#essa função calcula a hipotenusa de um triangulo retângulom, dado seus 2 catetos
#int, int, int -> float
    return math.sqrt(math.pow(b,2) + math.pow(c,2))

def calcularDistancia(x1,x2,y1,y2):
#essa função calcula a distancia de 2 pontos dados  seu pontos no plano cartesiano
#int, int, int -> float
    return math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))

def calcularPerimetroTrianguloReto(a,b,c):
#essa função calcula o perimetro de um triangulo reto
#int, int, int -> float
    return calcularHipotenusa(b,c) +  b + c

def calculaSeno(x):
#essa função faz a soma do seno ao quadrado com o cosseno ao quadrado e retorna o valor da soma
#int, int, int -> float
   return math.pow(math.sin(x),2) + math.pow(math.cos(x),2)

def calcularComprimentoCirculo(r):
#essa função calcula o comprimento de um circulo dado  seu raio.
#int, int, int -> float
    return 2*math.pi*r


