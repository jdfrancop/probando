
#caso 1
#try:
#    n1 = int(input("Ingresa un numero: "))
#    n2 = 2
#    print(n1)
#    print(n2)
#    print(n1/n2)
#except:
#    print("Entrada invalida, debe ser un tentero")

#caso 2

#try:
#    n1 = int(input("Ingresa un numero: "))
#    n2 = 0
#    print("Ingresaste el numero: ", n1)
#    print("el segundo numero es: ", n2)
#    print(n1/n2)
#except ZeroDivisionError:
#    print("No puedes dividir entre 0")
#except ValueError:
#    print("Entrada invalida, debe ser un tentero")
    

#caso 3

#try:
#    n1 = int(input("Ingresa un numero: "))
#    n2 = 0
#    print("Ingresaste el numero: ", n1)
#    print("el segundo numero es: ", n2)
#    print(n1/n2)
#except ZeroDivisionError as err:
#    print(err)
#except ValueError as err:
#    print(err)
    
try:
    n1 = int(input("Ingresa un numero: "))
    n2 = int(input("Ingresa otro numero: "))
    print("\nIngresaste el numero: ", n1)
    print("el segundo numero ingresado es: ", n2)
    print("El resultado de la division es: ", n1/n2)
except ZeroDivisionError as err:
    print("***ERROR***", err, "- No puedes dividir por cero")
except ValueError as err:
    print("***ERROR***", err, "\nDato invalido, debes ingresar un numero entero")
else:
    print("No hubo ningun error")
finally:
    print("Fin del programa")
        
    
    
    