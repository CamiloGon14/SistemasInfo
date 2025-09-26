from config.db import get_connection

class ClienteModel:
    @staticmethod
    def get_all():
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT nombre, direccion, numero FROM clientes")
            rows = cursor.fetchall()

            clientes = []
            for row in rows:
                clientes.append({
                    "nombre": row[0],
                    "direccion": row[1],
                    "numero": row[2]
                })

            conn.close()
            return clientes
        except Exception as e:
            raise Exception(f"Error fetching clientes: {str(e)}")
