def burbuja_asc(vec):
    tam = len(vec)

    for i in range(tam - 1):
        for j in range(tam - i - 1):
            if vec[j] > vec[j + 1]:
                # intercambio
                vec[j], vec[j + 1] = vec[j + 1], vec[j]


def burbuja_des(vec):
    tam = len(vec)

    for i in range(tam - 1):
        for j in range(tam - i - 1):
            if vec[j] < vec[j + 1]:
                # intercambio
                vec[j], vec[j + 1] = vec[j + 1], vec[j]

def burbuja_mejorado(vec):
    tam = len(vec)

    for i in range(tam - 1):
        intercambio = False
        for j in range(tam - i - 1):
            if vec[j].lower() >vec[j + 1].lower():
                vec[j], vec[j + 1] = vec[j + 1], vec[j]
                intercambio = True
        
        if intercambio == False:
            print(i)
            break

def burbuja_mejorado_numeros(vec):
    tam = len(vec)

    for i in range(tam - 1):
        intercambio = False
        for j in range(tam - i - 1):
            if vec[j] >vec[j + 1]:
                vec[j], vec[j + 1] = vec[j + 1], vec[j]
                intercambio = True
        
        if intercambio == False:
            print(i)
            break