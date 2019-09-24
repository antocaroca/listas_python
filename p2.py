"""
entregue una lista con los nombres de los pacientes que
se atendieron en los dias señalados
"""
fechas = {}
pacientes = {}
lista_rut_nombre = []
lista_rut = []

def pacientes_dia(dia, mes, ano):
    date = (f"{dia}-{mes}-{ano}")

    archivo_atenciones = open("atenciones.txt", "r")
    for line in archivo_atenciones:
        rut, fecha, precio = line.strip().split(":")
        if fecha not in fechas:
            fechas[fecha]=[]
        fechas[fecha].append(rut)
    #print('fechas:', fechas) # dicc fecha:rut
    for fecha, rut in fechas.items():
        #print(fecha, rut)
        if fecha == date:
            for i in rut:
                #print('rut:', i)
        
                archivo_pacientes = open("pacientes.txt", "r")
                for linea in archivo_pacientes:
                    pacientes = (linea.strip().split(":"))
                    lista_rut_nombre = (pacientes[0], pacientes[1]) # rut, nombre
                    if i == (lista_rut_nombre[0]):
                        print(lista_rut_nombre[1])

                       
pacientes_dia(24,10,2019)