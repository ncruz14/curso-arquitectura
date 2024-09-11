from model.cita import Cita
from view.vista_cita import mostrar_cita

def agendar_cita(paci, fecha, edad):
    cita = Cita(paci, fecha, edad)
    mostrar_cita(cita)
    
