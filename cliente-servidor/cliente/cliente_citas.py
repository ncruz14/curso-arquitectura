import socket

def solicitar_cita(id_cita):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(('localhost', 12345))  

    
    cliente.sendall(id_cita.encode())

    
    respuesta = cliente.recv(1024).decode()
    print(f"Respuesta del servidor: {respuesta}")

    cliente.close()  

if __name__ == "__main__":
    id_cita = input("Ingrese el ID de la cita que desea consultar: ")
    solicitar_cita(id_cita)
