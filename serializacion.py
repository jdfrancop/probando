import pickle
import os

estudiantes = [
    "Marcos",
    "Carla",
    "Agustin",
    "Pedro",
    "Maria"
]

serial = open("estudiantes", "wb")

pickle.dump(estudiantes, serial)

serial.close()
del serial

archivo = open("estudiantes", "rb")
lista1 = pickle.load(archivo)

print(lista1)

for i in lista1:
    print(i)





