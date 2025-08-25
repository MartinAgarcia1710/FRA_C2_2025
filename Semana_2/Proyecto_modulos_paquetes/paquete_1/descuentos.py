def aplicar_descuento(total:float)->float:
    if total >= 5000:
        return total * 0.9 #10% de descuento
    elif total >= 3000:
        return total * 0.95 #5% de descuento
    else:
        return total
    