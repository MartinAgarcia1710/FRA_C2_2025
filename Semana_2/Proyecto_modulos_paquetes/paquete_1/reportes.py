factura_numero = 1 

def mostrar_resumen(total:float, total_con_descuento: float) -> None:
    print(f"Total de la compra: {total}")
    print(f"Total a pagar con descuento: {total_con_descuento}")

def generar_ticket(monto:float)->None:
    global factura_numero
    print("===TICKET===")
    print(f"Factura Nro: {factura_numero}")
    print(f"Total a pagar: {monto}")
    print("============")
    factura_numero += 1

    


