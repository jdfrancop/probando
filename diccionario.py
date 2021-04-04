diccionario = {
                "a": 10,
                "b": 13,
                "c": 34   
    
}

print(diccionario)
print(diccionario["b"])
print(diccionario.get("a"))
print(diccionario.get("x", "No existe"))
print(diccionario.get("c", "No existe"))

diccionario.pop("b")
print(diccionario)

diccionario.popitem()
print(diccionario)

diccionario.update(a = 50)
diccionario.update(x = 50)
print(diccionario)

