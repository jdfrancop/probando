def saludo(nombre, edad):
    print("Hola " + nombre + " tienes " + edad + " años")

saludo("juan", "37")


suma = lambda n1, n2: n1 + n2
print("La suma es igual a: ", suma(30,60))

def multi(n1,n2):
    return n1*n2
print(multi(2,5))