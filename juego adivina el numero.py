import random

#variables a modificar
posibilidades = 10
limite = 30

print("Hola, ¿Como te llamas?")
nombre = input()

print("Muy bien " + nombre + " estoy pensando en un numero entre 1 y " + str(limite) + ", intenta adivinarlo")
print("A proposito, solo tienes " + str(posibilidades) + " posibilidades")

# Generamos un numero aleatorio entre 1 y limite
adivina = random.randint(1, limite)

intentos = 0

while intentos < posibilidades:
    num = int(input("Intenta adivinar: "))
    
    if num == adivina:
        print("GANASTE")
        break
    else:
        if num > adivina:
            print("Intenta con un numero mas pequeño")
        else:
            print("Intenta con un numero mas grande")
    intentos +=1
    
if num != adivina:
    print("PERDISTE")
    