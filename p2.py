"""
entregue una lista con los nombres de los pacientes que
 se atendieron en los dias señalados
"""
nombres = {}
fechas = {}
archivos = ("pacientes.txt", "atenciones.txt")

def pacientes_dia(dia, mes, ano):
    
    lista_rut = []
    date = (f"{dia}-{mes}-{ano}")

    archivo_atenciones = open("atenciones.txt", "r")
    for line in archivo_atenciones:
        rut, fecha, precio = line.strip().split(":")
        if fecha not in fechas:
            fechas[fecha]=[]
        fechas[fecha].append(rut)
    #print(fechas) # dicc fecha:rut
    for fecha, rut in fechas.items(): # aca se obtiene la fecha y rut segun fecha
        if fecha == date:
            #print(fecha, rut)
            lista_rut.append(rut)
            break
        else:
            print("[]")
            break
    archivo_atenciones.close()
    archivo_pacientes = open("pacientes.txt")
    for linea in archivo_pacientes:
        rut,nombre,edad = linea.strip().split(":")
    print(rut, nombre,edad)

    

                            
pacientes_dia(4, 5, 2010)