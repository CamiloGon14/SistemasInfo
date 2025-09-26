from flask import Flask
from routes.clienteRoutes import cliente_bp

app = Flask(__name__)

# Registrar el blueprint en /api
app.register_blueprint(cliente_bp, url_prefix="/api")

@app.route("/")
def home():
    return "✅ Flask conectado a SQL Server"

if __name__ == "__main__":
    # Mostrar todas las rutas registradas
    print("📌 Rutas registradas en Flask:")
    for rule in app.url_map.iter_rules():
        print(rule)
    app.run(debug=True)
