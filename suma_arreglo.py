#!/usr/bin/python3

#suma de arreglo

import random

def sumArreglo(x):
        arre = [ ]
        for i in range (x):
                arre.append(random.randint(1,1000))
        return arre

arreglo = sumArreglo(3)
print("El arreglo es:")
print(arreglo)

suma_repo = sum(arreglo)
print("La suma del arreglo es " + str(suma_repo))