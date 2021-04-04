lista =[0, 56, 6, 78, 4, 9, 12, 34, 56, 43, 87, 4]
lista.sort()

"""
1. buscar el punto medio
2. comprobar si el punto medio es el valor que buscamos
3. Si el numero es menor al valor que buscamos aumetamos inicio 1 sobre el
puntero
4. Si el numero es mayor al valor que buscamos disminuimos el final 1 sobre el
puntero
5. Si inicio si el inicio mayor o igual que final entonces el valor no se encuentra en la
lista
"""



def binaria(valor):
    inicio = 0
    fin = len(lista)-1
    while inicio <= fin:
        puntero = (inicio + fin) // 2
        if valor == lista[puntero]:
            return puntero
        elif valor > lista[puntero]:
            inicio = puntero + 1
        else:
            fin = puntero - 1
    return None

def buscar(valor):
    resultado = binaria(valor)
    if resultado is None:
        return f"El numero {valor} no fue encontrado"
    else:
        return f"El numero {valor} se encuentra en la posición {resultado}"
            
print(buscar(8))            
            
            
            
            
            
            
            
            
            
    
    
    
    
    
    
    
    
    
    
