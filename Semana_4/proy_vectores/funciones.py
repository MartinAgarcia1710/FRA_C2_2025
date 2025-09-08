import constantes

def cargar_notas_alumnos(i:int):
    print(f"Alumno: {i + 1}")
    programacion = float(input("Ingresar nota de programación I: "))
    matematica = float(input("Ingresar nota de Matemática: "))
    ingles = float(input("Ingresar nota de Ingles I: "))
    ayso = float(input("Ingresar nota de AYSO: "))
    return programacion, matematica, ingles, ayso

def calcular_promedio_alumno(prog, mate, ingl, ayso):
    return (prog + mate + ingl + ayso) / len(constantes.MATERIAS)

def mostrar_promedios_alumnos(vec_promedios_alumnos):
    print("Promedios generales de cada alumno")
    for i in range(constantes.CANTIDAD_ALUMNOS):
        print(f"Alumno: {i + 1}: {vec_promedios_alumnos[i]}")

def calcular_promedios_materias(vec_prog, vec_mate, vec_ingl, vec_ayso):
    vec_promedios = [0.0] * constantes.CANTIDAD_MATERIAS

    for j in range(constantes.CANTIDAD_ALUMNOS):
        vec_promedios[0] += vec_prog[j]
        vec_promedios[1] += vec_mate[j]
        vec_promedios[2] += vec_ingl[j]
        vec_promedios[3] += vec_ayso[j]

    for k in range(constantes.CANTIDAD_MATERIAS):
        vec_promedios[k] /= constantes.CANTIDAD_ALUMNOS

    return vec_promedios

def mostrar_promedios_materias(vec_promedio_materias):
    print("Promedios generales de materias")
    for k in range(constantes.CANTIDAD_MATERIAS):
        print(f"{constantes.MATERIAS[k]}: {vec_promedio_materias[k]:.2f}")


