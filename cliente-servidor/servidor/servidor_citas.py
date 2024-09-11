import socket
citas = {
    "1": {"paciente": "Juan Pérez", "fecha": "10/09/2024", "hora": "10:00 AM"},
    "2": {"paciente": "María Gómez", "fecha": "11/09/2024", "hora": "12:00 PM"},
}

def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(('localhost', 12345))  
    servidor.listen(1)  
    print("Servidor de citas iniciado, esperando solicitudes...")

    while True:
        conexion, direccion = servidor.accept()  
        print(f"Conexión establecida con {direccion}")

        
        solicitud = conexion.recv(1024).decode()
        print(f"Solicitud recibida: {solicitud}")

        
        respuesta = citas.get(solicitud, "Cita no encontrada")

        # Enviar respuesta al cliente
        conexion.sendall(str(respuesta).encode())
        conexion.close()  # Cierra la conexión

if __name__ == "__main__":
    iniciar_servidor()
