#!/usr/bin/python3

#suma de arreglo

import random

arreglo = [ ]

for i in range (3):
        arreglo.append(random.randint(1,1000))

print("El arreglo es:")
print(arreglo)

suma_repo = sum(arreglo)
print("La suma del arreglo es " + str(suma_repo))