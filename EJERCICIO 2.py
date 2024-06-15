# Ejercicio 2: Calculadora de Descuento 

edades = float(input("Ingrse Edad:"))
precio = 3000
if edades >= 18  and edades <= 65:
    descuento = precio * 0.85
    print(descuento)
elif edades < 18:
    descuento = precio * 0.90
    print(descuento)
else:
    print("No hay Descuento")