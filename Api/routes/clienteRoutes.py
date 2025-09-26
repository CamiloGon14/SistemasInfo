from flask import Blueprint
import controllers.clienteController as clienteController

cliente_bp = Blueprint("cliente_bp", __name__)

# 🔹 Rutas explícitas para cada operación
@cliente_bp.route("/get", methods=["GET"])
def get_all():
    return clienteController.get_clientes()

@cliente_bp.route("/get/<int:id>", methods=["GET"])
def get_one(id):
    return clienteController.get_cliente(id)

@cliente_bp.route("/create", methods=["POST"])
def create():
    return clienteController.create_cliente()

@cliente_bp.route("/update/<int:id>", methods=["PUT"])
def update(id):
    return clienteController.update_cliente(id)

@cliente_bp.route("/delete/<int:id>", methods=["DELETE"])
def delete(id):
    return clienteController.delete_cliente(id)
