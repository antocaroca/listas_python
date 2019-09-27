"""
Escribir una función ganancias_por_mes() que construya un nuevo archivo llamado ganancias.txt
que contenga el total de las ganancias por cada mes en el siguiente formato:
5-2010:933159
6-2010:1120967
7-2010:124903
17313888-1:4-5-2010:7500
"""
fechas = {}
def ganancias_por_mes():
    
    archivo_atenciones = open("atenciones.txt", "r")
    archivo_ganancias = open("ganancias.txt", "w")
    for linea in archivo_atenciones:
        rut, fecha, precio = linea.strip().split(":")
        fecha = fecha.split("-")
        fecha = ("-".join(fecha[1::]))
        # print(fecha, precio)
        if fecha not in fechas:
            fechas[fecha] = []
        fechas[fecha].append(precio)
    for fecha, precio in fechas.items():
        total = 0
        for i in precio:
            total += int(i)
        print(f"{fecha}:{total}")
        archivo_ganancias.write(f"{fecha}:{total}"+"\n")


ganancias_por_mes()