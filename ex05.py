import math

def calculaSetor(r,a =  360):
#essa função calcula o setor de um circulo dado o seu raio e o angulo do setor. caso o setor n seja informado ele assume o valor de 360 por padrão
#int, int, int -> float
    return (a*math.pi*math.pow(r, 2))/360

