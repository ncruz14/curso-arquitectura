from events.evento_cita import EventoCitaCreada

def crear_cita(paciente, fecha):

    evento = EventoCitaCreada(paciente, fecha)
    return evento
