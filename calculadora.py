import tkinter as tk
from tkinter import messagebox
 
def sumar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        suma = num1 + num2
        messagebox.showinfo("Resultado", f"La suma es: {suma}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")

def resta():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resta = num1 - num2
        messagebox.showinfo("Resultado", f"La resta es: {resta}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")
 
 

def division():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        division = num1/num2
        messagebox.showinfo("Resultado", f"La division es: {division}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")

def multiplicacion():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        multiplicacion = num1*num2
        messagebox.showinfo("Resultado", f"La multiplicacion es: {multiplicacion}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")
 
 
ventana = tk.Tk()
ventana.title("Calculadora de Suma")
ventana.geometry("300x400")
 
label_num1 = tk.Label(ventana, text="Número 1:")
label_num1.pack(pady=5)
entry_num1 = tk.Entry(ventana)
entry_num1.pack(pady=5)
 
label_num2 = tk.Label(ventana, text="Número 2:")
label_num2.pack(pady=5)
entry_num2 = tk.Entry(ventana)
entry_num2.pack(pady=5)
 
boton_sumar = tk.Button(ventana, text="Sumar", command=sumar)
boton_sumar.pack(pady=20)
 
 
boton_resta = tk.Button(ventana, text="Resta", command=resta)
boton_resta.pack(pady=20)
 
boton_resta = tk.Button(ventana, text="Division", command=division)
boton_resta.pack(pady=20)
 
boton_resta = tk.Button(ventana, text="Multiplicacion", command=multiplicacion)
boton_resta.pack(pady=20)
 
ventana.mainloop()
 
 
 