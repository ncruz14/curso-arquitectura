from view.ui import mostrar_paciente
from business.gestion_citas import registrar_paciente
from data.acceso_datos import guardar_paciente

if __name__ == "__main__":
    nombre = "Nathalia"
    guardar_paciente(nombre)  
    mostrar_paciente(nombre)  
    resultado = registrar_paciente(nombre)  
    print(resultado)
