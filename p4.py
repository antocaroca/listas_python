"""
Escribir una función ganancias_por_mes() que construya un nuevo archivo llamado ganancias.txt
que contenga el total de las ganancias por cada mes en el siguiente formato:
5-2010:933159
6-2010:1120967
7-2010:124903
17313888-1:4-5-2010:7500
"""
fechas = {}
nueva_fecha = []
def ganancias_por_mes():
    total = 0
    archivo_atenciones = open("atenciones.txt", "r")
    archivo_ganancias = open("ganancias.txt", "w")
    for linea in archivo_atenciones:
        rut, fecha, precio = linea.strip().split(":")
        if fecha not in fechas:
            fechas[fecha]= []
        fechas[fecha].append(precio)
    #print(fechas)
    for fecha, precio in fechas.items():
        fecha = fecha.split("-")
        fecha = "-".join(fecha[1::])
        #print(fecha)
        for i in precio:
            total += int(i)
            archivo_ganancias.write(f"{fecha}:{total}"+"\n")
        

ganancias_por_mes()

# HAY QUE SEPARAR LOS VALORES DE ACUERDO A CADA FECHA PORQUE SUMA TODO VALOR TRAS VALOR.