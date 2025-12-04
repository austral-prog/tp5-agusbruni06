def number_to_month(month):
    meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    if 1 <= month <= 12:
        return meses[month - 1]
    else:
        return "error"

ingreso = int(input("Ingrese un número del 1 al 12: "))
print(number_to_month(ingreso))
