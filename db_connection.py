import mysql.connector

def connect_db():
    try:
        conn = mysql.connector.connect(
            host="bhpcw7xr6yo5qhopcadr-mysql.services.clever-cloud.com",        # Cambia si tu host es diferente
            user="uxibc4wewbdlw4ck",       # El usuario que tiene acceso a la base de datos
            password="Z7NCbwQlWkKVStxYBKgP", # La contraseña del usuario
            database="bhpcw7xr6yo5qhopcadr" # El nombre de la base de datos que usarás
        )
        if conn.is_connected():
            print("Conexión exitosa a la base de datos")
        return conn
    except mysql.connector.Error as err:
        print(f"Error al conectarse: {err}")
        return None

        
