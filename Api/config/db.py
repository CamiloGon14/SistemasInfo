import pyodbc

def get_connection():
    try:
        connection = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=localhost,1433;"
            "DATABASE=huevos_sofi;"
            "UID=sa;"
            "PWD=123;"
            "TrustServerCertificate=yes;"
        )
        return connection
    except pyodbc.Error as e:
        raise Exception(f"Database connection failed: {str(e)}")
