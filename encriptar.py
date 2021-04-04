#version 1

#def encriptar(frase):
#    encriptada = ""
#    for letra in frase:
#        if letra in "AEIOUaeiou":
#            encriptada = encriptada + "x"
#        else:
#            encriptada = encriptada + letra
#    return encriptada

#print(encriptar(input("Ingresa una frase: \n>>> ")))

print("----------------------------------------------------")

# version 2

#caracter1 = "x"

#def encriptar(frase, caracter):
#    encriptada = ""
#    for letra in frase:
#        if letra in "AEIOUaeiou":
#            if letra.isupper():
#                encriptada = encriptada + caracter1.upper()
#            else:
#                encriptada = encriptada + caracter1
#        else:
#            encriptada = encriptada + letra
#    return encriptada

#print(encriptar(input("Ingresa una frase: \n>>> "),caracter1))

print("----------------------------------------------------")

# version 3

caracter1 = "x"

def encriptar(frase, caracter):
    encriptada = ""
    for letra in frase:
        if letra.lower() in "aeiou":
            if letra.isupper():
                encriptada = encriptada + caracter1.upper()
            else:
                encriptada = encriptada + caracter1
        else:
            encriptada = encriptada + letra
    return encriptada

while True:
    print(encriptar(input("Ingresa una frase: \n>>> "),caracter1))
    
    print("\nIngresa: (1) para encriptar otra frase")
    print("(2) para finalizar")
    opcion = input("--- ")
    if opcion == "2":
        print("ADIOS")
        break
    if opcion == "1":
        print("********* \n")


    