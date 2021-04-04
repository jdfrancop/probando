a = open("estudiantes.txt", "r")

# Lectura
#print(a.read())
print("----------")
# print(a.readline())
# print(a.readlines())
#print(a.readlines()[3])
#for i in a:
#    print(i)
a.close

print("----------")

# Escribir

# a = open("nombres.txt", "w")
# print(a.write("Que bonito que \n funcione, jejjeje"))

# a = open("nombres.txt", "a")
# print(a.write("Que bonito que \n funcione, jejjeje"))

# a = open("nombres.txt", "a")
# print(a.write("\nQue bonito que \n funcione, jejjeje"))
a.close

print("----------")

# Eliminar archivo

import os
os.remove("nombres.txt")
