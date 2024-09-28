import tkinter as tk
from tkinter import messagebox
from db_connection import connect_db  # Importar la función de conexión
import mysql.connector
import tkinter as tk
from tkinter import messagebox


# Función para registrar un nuevo usuario
def register_user():
    username = entry_username.get()
    password = entry_password.get()

    if username and password:
        try:
            conn = connect_db()
            cursor = conn.cursor()

            cursor.execute(
                "INSERT INTO users (username, password) VALUES (%s, %s)",
                (username, password),
            )
            conn.commit()

            messagebox.showinfo("Registro", "Usuario registrado con éxito")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"No se pudo registrar: {err}")
        finally:
            if conn:
                conn.close()
    else:
        messagebox.showwarning(
            "Datos faltantes", "Por favor, completa todos los campos."
        )


# Función para iniciar sesión
def login_user():
    username = entry_username.get()
    password = entry_password.get()

    if username and password:
        try:
            conn = connect_db()
            cursor = conn.cursor()

            # Comprobar si el usuario y contraseña coinciden
            cursor.execute(
                "SELECT * FROM users WHERE username = %s AND password = %s",
                (username, password),
            )
            result = cursor.fetchone()

            if result:
                messagebox.showinfo("Inicio de sesión", f"Bienvenido {username}")
            else:
                messagebox.showwarning(
                    "Error de inicio de sesión", "Usuario o contraseña incorrectos"
                )
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error al iniciar sesión: {err}")
        finally:
            if conn:
                conn.close()
    else:
        messagebox.showwarning(
            "Datos faltantes", "Por favor, completa todos los campos."
        )


# Configuración de la interfaz gráfica con Tkinter
root = tk.Tk()
root.title("Sistema de Registro e Inicio de Sesión")

# Etiquetas y campos de entrada
label_username = tk.Label(root, text="Usuario")
label_username.pack()

entry_username = tk.Entry(root)
entry_username.pack()

label_password = tk.Label(root, text="Contraseña")
label_password.pack()

entry_password = tk.Entry(root, show="*")
entry_password.pack()

# Botón para registrar usuario
button_register = tk.Button(root, text="Registrar", command=register_user)
button_register.pack()

# Botón para iniciar sesión
button_login = tk.Button(root, text="Iniciar Sesión", command=login_user)
button_login.pack()

root.mainloop()
