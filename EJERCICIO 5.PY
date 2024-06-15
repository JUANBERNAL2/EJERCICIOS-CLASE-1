salario = float(input("Ingrese salario:"))
if salario <= 10000:
    print(salario)
elif salario <= 50000:
    impuesto = salario * 0.90
    print(impuesto)
elif salario <= 100000:
    impuesto = salario * 0.80
    print(impuesto)
else:
    impuesto = salario * 0.70
    print(impuesto)