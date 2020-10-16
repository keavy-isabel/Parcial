import math

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la suma de 3 numeros
2+4+6 = 12
"""


# start-->
def suma(numero1, numero2, numero3):
    adicion = numero1 + numero2 + numero3
    return adicion


"""
***************************************************************
@@ ejercicio 2 @@
la suma de los numeros impares del 1 al 1000
"""


# start-->
def sumaImpares():
    iterator = 0
    result = 0
    while iterator < 1000:
        if iterator%2 == 0:
            iterator += 1
        else:
            result += iterator
            iterator += 1
    return result

"""
***************************************************************
@@ ejercicio 3 @@
encontrar el perimetro, area y el volumen de un esfera
radio = 12 m

perimetro: 2*pi*r
area: 4*pi*r^2
volumen: (4/3)*pi*r^3
"""


# start-->
def definicionEsfera(r):
    result = {"perimetro": obtenerPerimetro(), "area":obtenerArea(), "volumen":obtenerVolumen()}
    return result


def obtenerPerimetro(r):
    result = 2*math.pi*r
    return result


def obtenerArea(r):
    result = 4*math.pi*r*r
    return result


def obtenerVolumen(r):
    result = (4/3)*math.pi*r*r*r
    return result


"""
***************************************************************
@@ ejercicio 4 @@
el ejercicio numero 3 convertirlo en una clase

"""


# start-->
class Esfera:
    def __init__definicionEsfera(self , r):
        self.r = r
    def obtenerPerimetro(self):
        result = 2*math.pi*r
        return result


    def obtenerArea(self):
        result = 4*math.pi*r*r
        return result


    def obtenerVolumen(self):
        result = (4/3)*math.pi*r*r*r
        return result



"""
***************************************************************
@@ ejercicio 5 @@
Banco
Cliente
    nombre
    lugar
    numero de cuenta
    transaccion - retiro o abono
    monto
"""


class Banco:

    def procesar(self, nombre, lugar, numcuenta, transaccion, monto):
        self.nombre = nombre
        self.departamento = departamento
        self.numcuenta = numcuenta
        self.transaccion = transaccion
        self.monto = monto
        return 0

    def abonosSanSalvador(self):
        return 0

    def abonosBalYRod(self):
        return 0


class Cliente:
    pass


"""
***************************************************************
@@ ejercicio 6 @@
colocar este proyecto en github
colocar aca debajo la url
ademas colocar la url en un archivo
github_<nombre>_<codigo>.txt y subirlo a moodle
"""


# github url-->
def getGithubUrl():
    return ""
