from flask import jsonify, request
from config.db import get_connection

# 🔹 Obtener todos los clientes
def get_clientes():
    conexion = get_connection()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre, direccion, numero FROM clientes")
    clientes = cursor.fetchall()
    cursor.close()
    conexion.close()

    resultado = []
    for fila in clientes:
        resultado.append({
            "id": fila[0],
            "nombre": fila[1],
            "direccion": fila[2],
            "numero": fila[3]
        })
    return jsonify(resultado), 200

# 🔹 Obtener un cliente por ID
def get_cliente(id):
    conexion = get_connection()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre, direccion, numero FROM clientes WHERE id = ?", (id,))
    fila = cursor.fetchone()
    cursor.close()
    conexion.close()

    if fila:
        return jsonify({
            "id": fila[0],
            "nombre": fila[1],
            "direccion": fila[2],
            "numero": fila[3]
        }), 200
    else:
        return jsonify({"mensaje": "Cliente no encontrado"}), 404

# 🔹 Crear un cliente nuevo
def create_cliente():
    data = request.get_json()
    conexion = get_connection()
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO clientes (nombre, direccion, numero) VALUES (?, ?, ?)",
        (data["nombre"], data["direccion"], data["numero"])
    )
    conexion.commit()
    cursor.close()
    conexion.close()
    return jsonify({"mensaje": "Cliente creado con éxito"}), 201

# 🔹 Actualizar un cliente por ID
def update_cliente(id):
    data = request.get_json()
    conexion = get_connection()
    cursor = conexion.cursor()
    cursor.execute(
        "UPDATE clientes SET nombre=?, direccion=?, numero=? WHERE id=?",
        (data["nombre"], data["direccion"], data["numero"], id)
    )
    conexion.commit()
    cursor.close()
    conexion.close()
    return jsonify({"mensaje": "Cliente actualizado con éxito"}), 200

# 🔹 Eliminar un cliente por ID
def delete_cliente(id):
    conexion = get_connection()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM clientes WHERE id=?", (id,))
    conexion.commit()
    cursor.close()
    conexion.close()
    return jsonify({"mensaje": "Cliente eliminado con éxito"}), 200
