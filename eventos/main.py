from services.servicio_citas import crear_cita
from handlers.manejador_notificaciones import enviar_notificacion

if __name__ == "__main__":
    # Crear una cita (desencadenar el evento)
    evento = crear_cita("Juan Pérez", "10/09/2024")
    
    # Manejar el evento (enviar notificación)
    enviar_notificacion(evento)
