from paquete_1.utilidades import saludar as PU
from paquete_1.calculos import calcular_subtotal as PC
from paquete_1.descuentos import aplicar_descuento as PD
from paquete_1.reportes import mostrar_resumen, generar_ticket as PR
print("-----Bienvenidos a la tienda-----")

conocido = input("El cliente está registrado? (s/n)")

if conocido == 's':
    nombre = input("Ingrese nombre: ")
    PU.saludar(nombre)
else:
    PU.saludar()

total:float = 0.0 #acumulador de la venta

for x in range(3):
    precio: float = float(input("Ingresar precio UNITARIO del producto"))
    cantidad: int = int(input("Ingresar cantidad: "))
    subtotal: float = PC.calcular_subtotal(precio, cantidad)
    print(f"Subtotal del producto: {subtotal}")
    total += subtotal

total_con_descuento: float = PD.aplicar_descuento(total)

PR.mostrar_resumen(total, total_con_descuento)
PR.generar_ticket(total_con_descuento)
