import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import messagebox
from excepciones.excepciones import PrecioNegativaEx, ProductoInvalidoEx, CantidadNegativaEx
from productos.productos import Producto

def agregar_producto():
    try:
        nombre = entry_nombre.get()
        precio = float(entry_precio.get())
        cantidad = int(entry_cantidad.get())

        producto = Producto(nombre, precio, cantidad)
        detalles = producto.mostrar_detalles_compra()

        text_resultado.delete(1.0, tk.END)
        text_resultado.insert(tk.END, detalles)

    except ValueError:
        messagebox.showerror("Error", "Precio y cantidad deben ser números válidos.")
    except ProductoInvalidoEx as e:
        messagebox.showerror("Error", str(e))
    except PrecioNegativaEx as e:
        messagebox.showerror("Error", str(e))
    except CantidadNegativaEx as e:
        messagebox.showerror("Error", str(e))

ventana = tk.Tk()
ventana.title("Sistema de Gestión de Productos")
ventana.geometry("500x400")
ventana.config(bg="#4B0082")  


label_nombre = tk.Label(ventana, text="Nombre del Producto:", bg="#4B0082", fg="#FF6347", font=("lato", 12))
label_nombre.pack(pady=5)
entry_nombre = tk.Entry(ventana, font=("lato", 12), bg="#FFF0F5", fg="#000000")
entry_nombre.pack(pady=5)

label_precio = tk.Label(ventana, text="Precio del Producto:", bg="#4B0082", fg="#FF6347", font=("lato", 12))
label_precio.pack(pady=5)
entry_precio = tk.Entry(ventana, font=("lato", 12), bg="#FFF0F5", fg="#000000")
entry_precio.pack(pady=5)

label_cantidad = tk.Label(ventana, text="Cantidad que lleva:", bg="#4B0082", fg="#FF6347", font=("lato", 12))
label_cantidad.pack(pady=5)
entry_cantidad = tk.Entry(ventana, font=("lato", 12), bg="#FFF0F5", fg="#000000")
entry_cantidad.pack(pady=5)


boton_agregar = tk.Button(ventana, text="Agregar Producto", command=agregar_producto, bg="#FF6347", fg="#FFFFFF", font=("lato", 12))
boton_agregar.pack(pady=10)


text_resultado = tk.Text(ventana, height=10, width=40, font=("lato", 12), bg="#FFF0F5", fg="#000000")
text_resultado.pack(pady=10)

ventana.mainloop()
