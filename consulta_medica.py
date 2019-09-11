costo_final = {}

def costo_total_paciente(rutAtenciones):
    archivo = open("atenciones.txt", "r")
    
    for linea in archivo:
        rut, fecha, precio = linea.strip().split(":")
        if rut not in costo_final:
            costo_final[rut] = []
        costo_final[rut].append(int(precio))
        total_a_pagar = 0
        for i in (costo_final[rutAtenciones]):
            total_a_pagar += i
    print(f"Total a pagar: {total_a_pagar}")  
      
    archivo.close()

costo_total_paciente("17313888-1")