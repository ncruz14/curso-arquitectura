# servicio_notificaciones/app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulación de envío de notificaciones
@app.route('/enviar_notificacion', methods=['POST'])
def enviar_notificacion():
    data = request.get_json()
    paciente = data['paciente']
    accion = data['accion']  # 'creada', 'modificada', 'cancelada'
    mensaje = f"Su cita ha sido {accion}."
    print(f"Notificación enviada a {paciente}: {mensaje}")
    return jsonify({"mensaje": "Notificación enviada"}), 200

if __name__ == '__main__':
    app.run(port=5001, debug=True)
