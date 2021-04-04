class Estudiante:
    def __init__(self, nombre, edad, curso_inicial):
        self.nombre = nombre
        self.edad = edad
        self.curso_inicial = curso_inicial
        self.estado_activo = True
        self.cursos = [curso_inicial]


estudiante1 = Estudiante("Juan", 34, "Python")

estudiante1.edad = 45

print(estudiante1.nombre)





