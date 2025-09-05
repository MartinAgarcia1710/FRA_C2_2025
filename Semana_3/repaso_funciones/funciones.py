def pedir_turno():
    nombre = input("Ingresar nombere: ")
    turno = input("Ingresar turno (d/n):")
    return nombre, turno

def registrar_turno(nombre, turno):
    if turno == "d" or turno == "n":
        return f"Turno registrado: {nombre} trabajará en turno {turno}"
    else:
        return "Turno inválido, solo se permite d o n"
    
def pedir_pago():
    horas = int(input("Ingrese cantidad de hs trabajadas: "))
    turno = input("Ingrese turno trabajado (d/n)")
    return horas, turno

def calcular_pago(horas, turno):
    if turno == "d":
        return horas * 100
    elif turno == "n":
        return horas *150
    else:
        return 0
    
    
def mensaje_agradecimiento():
    print("gracias por utilizar el sistema")