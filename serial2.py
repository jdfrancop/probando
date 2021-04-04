import pickle
import os

class Estudiante:
    def __init__(self, nombre, edad, curso_inicial):
        self.nombre = nombre
        self.edad = edad
        self.curso_inicial = curso_inicial
        self.estado_activo = True
        self.cursos = [curso_inicial]
    
    def desactivar(self):
        self.estado_activo = False
        
    def info(self):
        print(f"Estudiante: {self.nombre}\n Edad: {self.edad}\nEstado: {self.estado_activo}\n")
    
est1 = Estudiante("Julian", 45, "AWS")
est2 = Estudiante("Cris", 23, "Python")
est3 = Estudiante("Juan", 19, "Java")

lista_est_obj = [
    est1,
    est2,
    est3
]

archivo_est_obj = open("estudiantes_obj", "wb")
pickle.dump(lista_est_obj, archivo_est_obj)

archivo_est_obj.close()
del archivo_est_obj

archivo_est = open("estudiantes_obj", "rb")
lista_estudiantes_obj = pickle.load(archivo_est)



for e in lista_estudiantes_obj:
    """print(e)
    print(e.nombre)
    print(e.edad)
    print(e.curso_inicial)"""
    print(e.info())
    
    
    