numeros = [1,2,3,4,5,6]

frutas = ["naranja", "Fresa", "manzana", "uva","pera"]
print(frutas)
print(frutas[3])
print(frutas[-2])

lista = list((1,2,3,"hola","dos",5))
print(lista)


nueva = numeros + frutas + lista
print(nueva)

nueva2 = [0]
nueva2.extend(numeros)
print(nueva2)

nueva2.insert(2,8)
print(nueva2)
saludo = ["holi","hola","hola","hola","hola","hola","hola"]
nueva2.remove(8)
print(nueva2)

print(frutas.index("uva"))
print(saludo.index("hola"))
print(nueva.count(1))
print(saludo.count("hola"))

frutas.sort()
print(frutas)

tua = (8,4,6)

print(tua)