
import tkinter as tk
from tkinter import messagebox
import mysql.connector
 
def verificar_usuario():
    correo = entry_correo.get()
    contraseña = entry_contraseña.get()
 
    try:
        conn = mysql.connector.connect(
            host='localhost',      
            user='root',          
            password='',  
            database='clasestec'    
            )
 
        cursor = conn.cursor()
 
        cursor.execute('''
            SELECT * FROM usuarios WHERE correo = %s AND contraseña = %s
        ''', (correo, contraseña))
 
        usuario = cursor.fetchone()
 
        if usuario:
            messagebox.showinfo("Login exitoso", f"Bienvenido {usuario[1]}")
        else:
            messagebox.showerror("Error", "Usuario o contraseña no encontrados.")
   
    except mysql.connector.Error as err:
        messagebox.showerror("Error de conexión", f"Error: {err}")
   
    finally:
        if conn.is_connected():
            conn.close()  
 
root = tk.Tk()
root.title("Login")
root.geometry("300x200")
 
label_correo = tk.Label(root, text="Correo:")
label_correo.pack(pady=5)
entry_correo = tk.Entry(root, width=30)
entry_correo.pack(pady=5)
 
label_contraseña = tk.Label(root, text="Contraseña:")
label_contraseña.pack(pady=5)
entry_contraseña = tk.Entry(root, width=30, show="*")
entry_contraseña.pack(pady=5)
 
btn_login = tk.Button(root, text="Login", command=verificar_usuario)
btn_login.pack(pady=20)
 
root.mainloop()
 
 