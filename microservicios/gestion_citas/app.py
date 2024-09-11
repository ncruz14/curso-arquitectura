
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

citas = {}


@app.route('/crear_cita', methods=['POST'])
def crear_cita():
    data = request.get_json()
    id_cita = str(len(citas) + 1)
    citas[id_cita] = {
        'paciente': data['paciente'],
        'fecha': data['fecha'],
        'hora': data['hora']
    }
    
    
    notificacion_data = {'paciente': data['paciente'], 'accion': 'creada'}
    requests.post('http://localhost:5001/enviar_notificacion', json=notificacion_data)
    
    return jsonify({"mensaje": f"Cita creada con ID {id_cita}"}), 201

if __name__ == '__main__':
    app.run(port=5000, debug=True)
