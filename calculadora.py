num1 = float(input("Ingresa un numero: "))
num2 = float(input("Ingresa otro numero:" ))
op = input("Ingresa un operador: ")

if op == "+":
    res = num1 + num2
    print("La suma es: " , res)
elif op == "-":
    res = num1 - num2
    print("La resta es: " , res)
elif op == "*":
    res = num1 * num2
    print("La multiplicación es: " , res)
elif op == "/":
    res = num1 / num2
    print("La división es: " , res)
else:
    print("El operador es invalido")