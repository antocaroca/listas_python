"""
entregue una lista con los nombres de los pacientes que
 se atendieron en los dias señalados
"""
nombres = {}
pacientes = {}
pacientes_atencion = {}
archivos = ("atenciones.txt", "pacientes.txt")

def pacientes_dia(dia, mes, ano):
    archivo_atenciones = open("atenciones.txt", "r")
    archivo_pacientes = open("pacientes.txt", "r")

    date = f"{dia}-{mes}-{ano}"
    rut_atenciones = []

    for line in archivo_atenciones:
        rut, fecha, precio = line.strip().split(":")
        if fecha == date:
            rut_atenciones.append(rut)
    # print(rut_atenciones)

    rut_pacientes = []
    
    for linea in archivo_pacientes:
        rut, nombre, edad = linea.strip().split(":")
        rut_pacientes.append((rut, nombre))
    print(rut_pacientes)

    # for i in rut_pacientes: #lista rut y nombre
    #     print(i)
        # for j in rut_atenciones:
        #     if (i[0]) == j:
        #         print(i[1])
        

    
pacientes_dia(11,10,2019)