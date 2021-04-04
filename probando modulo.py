import pickle
from serial2 import Estudiante

archivo_est = open("estudiantes_obj", "rb")
lista_estudiantes_obj = pickle.load(archivo_est)


