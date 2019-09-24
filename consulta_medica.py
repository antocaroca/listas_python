costo_final = {}

def costo_total_paciente(rutAtenciones):
    archivo = open("atenciones.txt", "r")

    for linea in archivo:
        rut, fecha, precio = linea.strip().split(":")
        if rut not in costo_final:
            costo_final[rut] = []
        costo_final[rut].append(int(precio))
    print(sum(costo_final[rutAtenciones]))

        
    archivo.close()

costo_total_paciente("17313888-1")