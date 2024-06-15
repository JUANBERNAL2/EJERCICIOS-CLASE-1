puntaje = float(input("Ingrse puntuacion:"))

if puntaje >= 90:
    print("SOBRESALIENTE")
elif puntaje >= 80:
    print("Bueno")
elif puntaje >= 70:
    print("Satisfactorio")
elif puntaje >= 60:
    print("Nesecitas mejorar")
else:
    print("REPROBADO")