cadena = "los Dias de nuEstras vidas"
letra = cadena[5]
print(letra)
letra = cadena[-5]
print(letra)
letras = cadena[2:9]
print(letras)

modificado = cadena.capitalize()
print(modificado)

alumnos = 2500
academia = "sena "
cadena2 = "los " + str(alumnos) + " alumnos del " + academia + "son muy aplicados"
print(cadena2)

cadena3 = "los   {} alumnos de {} son muy aplicados".format(alumnos,academia)
print(cadena3)

