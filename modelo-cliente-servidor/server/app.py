from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

tareas = []

@app.route('/tareas', methods=['POST'])
def add_tarea():
    tarea = request.json.get('tarea')
    tareas.append(tarea)
    return jsonify({'message': 'Tarea añadida con éxito'}), 200

@app.route('/tareas', methods=['GET'])
def get_tareas():
    return jsonify(tareas), 200

@app.route('/tareas',methods=['DELETE'])
def delete_tareas():
    global tareas
    tareas.clear()
    return jsonify({'message': 'Tareas eliminadas'}), 200

if __name__ == '__main__':
    app.run()
