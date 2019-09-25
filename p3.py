"""
Escriba la función separar_pacientes() que construya dos nuevos archivos: 
- jovenes.txt, con los datos de los pacientes menores de 30 años
- mayores.txt, con los datos de los pacientes mayores de 60 años
Por ejemplo, jovenes.txt:
15007265-4:Andrés Morales:26
"""
edades = {}
edad_jovenes = ""
edad_mayores = ""
def separar_pacientes():
    jovenes = open("jovenes.txt", "w")
    mayores = open("mayores.txt", "w")
    archivo_pacientes = open("pacientes.txt", "r")
    for linea in archivo_pacientes:
        edades = (linea.strip().split(":"))
        if (int(edades[2])) < 30:
            edad_jovenes = (":".join(edades))
            #print(edad_jovenes)
            jovenes.write(edad_jovenes + "\n")
        elif int(edades[2]) > 60:
            edad_mayores = (":".join(edades))
            #print(edad_mayores)
            mayores.write(edad_mayores + "\n")

                
separar_pacientes()