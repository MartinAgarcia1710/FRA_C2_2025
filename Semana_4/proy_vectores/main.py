# Realizar un programa para cargar las notas de 4 materias que se dictan en el cuatrimestre. 
# La cantidad de alumnos es 20.
# Mostrar el promedio general de cada alumno
# Además, mostrar el promedio general del curso de cada materia.
# Las materias son: Programación I, Matemática, Inglés I y AySO.

import constantes
import funciones as fn

vec_prog = [0.0] *constantes.CANTIDAD_ALUMNOS
vec_mate = [0.0] *constantes.CANTIDAD_ALUMNOS
vec_ingl = [0.0] *constantes.CANTIDAD_ALUMNOS
vec_ayso = [0.0] *constantes.CANTIDAD_ALUMNOS
vec_promedios_alumnos = [0.0] * constantes.CANTIDAD_ALUMNOS

for i in range(constantes.CANTIDAD_ALUMNOS):
    prog, mate, ingl, ayso = fn.cargar_notas_alumnos(i)
    vec_prog[i] = prog
    vec_mate[i] = mate
    vec_ingl[i] = ingl
    vec_ayso[i] = ayso

    vec_promedios_alumnos[i] = fn.calcular_promedio_alumno(prog, mate, ingl, ayso)

fn.mostrar_promedios_alumnos(vec_promedios_alumnos)

vec_promedio_materias = fn.calcular_promedios_materias(vec_prog, vec_mate, vec_ingl, vec_ayso)

fn.mostrar_promedios_materias(vec_promedio_materias)


