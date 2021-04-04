hombre = True
alto = True

if hombre and alto:
    print("Eres un hombre alto")
elif hombre and not alto:
    print("Eres un hombre bajo")
elif not hombre and alto:
    print("No eres un hombre, pero eres alto")
else:
    print("No eres un hombre y tampoco eres alto")
    
#------------------------------------------------------
    
def mayor_edad(num):
    if num>=18:
        return True
    else:
        return False
    
edad = input("Ingresa tu edad: ")

if mayor_edad(int(edad)):
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
    
    
#-------------------------------------------------

def mayor(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    if n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3
print(mayor(20,7,100))