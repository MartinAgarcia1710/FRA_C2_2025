# Realizar un peqieño sistema de gestión en consola para que una 
# concecionaria pueda cargar ventas, la misma se detiene cuando se
# ingresa 0. El programa debe informar al finalizar:
#              1. La venta mayor
#              2. La venta menor
#              3. Cantidad de ventas realizadas
#              4. El total de ventas

# Iniciación de variables
total_ventas = 0 #acumulador (incrementar por montos de venta)
cantidad_ventas = 0 #contador (incrementar de a uno)
venta_mayor = None #Se va a guardar la ventan de mayor monto
venta_menor = None # Se va a guardar la venta de menor monto

while True:
    # (ENTRADA) Ingreso de ventas
    venta = float(input("Ingresar venta (Para finalizar ingresar 0): "))
    # Corte de ciclo
    if venta == 0:
        break
    
    # (PROCESOS) Acumulamos ventas y contamos ventas
    total_ventas += venta
    cantidad_ventas += 1

    # (PROCESO) Buscamos mayor y menor

    if cantidad_ventas == 1: # Condicional que inicia de base nuestras variables
        venta_mayor = venta
        venta_menor = venta
    else:
        # Condicional interno que compara mayores
        if venta > venta_mayor:
            venta_mayor = venta
        # Segundo condicional interno que compara menores
        if venta < venta_menor:
            venta_menor = venta

# (PROCESO) Calculamos promedio de ventas
promedio_ventas = total_ventas / cantidad_ventas


# (SALIDA) Se muestran los valores

print(f"Toral de ventas realizadas: {cantidad_ventas} con un monto de: {total_ventas}")

# Validación de existencia de ventas para muestra de mayor, menor y promedio
if cantidad_ventas > 0:
    print(f"Venta mayor: {venta_mayor}")
    print(f"Venta menor: {venta_menor}")
    print(f"El promedio de ventas es: {promedio_ventas}")
else:
    print("No se registraron ventas mayores o menores...")

