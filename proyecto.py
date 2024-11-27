
import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector
from tkinter import *

#! VENTANA DE ADMIN

def mostrar_gestion_empleados():
    ventana_principal = tk.Toplevel()
    ventana_principal.title("Gestion de Empleados")
    ventana_principal.destroy()
    
    def mostrar():
        mysqlC = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "proyecto")
        micursos = mysqlC.cursor()
        micursos.execute("select * from usuarios")
        lista = micursos.fetchall() 
        
        for i,(id, nombre, apellido, usuario, contraseña, rol) in enumerate(lista, start = 1):
            listbox.insert("", "end", values = (id, nombre, apellido, usuario, contraseña, rol))
            mysqlC.close()

    def add():
        nombreAdd = name.get()
        apellidoAdd = lastname.get()
        usuarioAdd = user.get()
        contraAdd = password.get()
        rolAdd = role_add.get()
        idAdd = identificador.get()
        mysqlC = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "proyecto")
        micursos = mysqlC.cursor()
        try:
            micursos.execute(f"insert into usuarios (id, nombre, apellido, usuario, contraseña, rol) values('{idAdd}','{nombreAdd}','{apellidoAdd}','{usuarioAdd}','{contraAdd}','{rolAdd}')")
            mysqlC.commit()
            name.delete(0, END)
            lastname.delete(0, END)
            user.delete(0, END)
            password.delete(0, END)
            role.delete(0, END)
            identificador.delete(0, END)
            messagebox.showinfo("informacion", "empleado agregado")
            actualizar()
            
        except Exception as e:
            print(e)
            mysqlC.rollback()
            mysqlC.close()

    def actualizar():
        for i in listbox.get_children():
            listbox.delete(i)
        mostrar()

    def delete():
        idAdd = identificador.get()
        mysqlC = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "proyecto")
        micursos = mysqlC.cursor()
        try:
            micursos.execute(f"DELETE FROM USUARIOS WHERE id = {idAdd}")
            mysqlC.commit()
            name.delete(0, END)
            lastname.delete(0, END)
            user.delete(0, END)
            password.delete(0, END)
            role.delete(0, END)
            identificador.delete(0, END)
            messagebox.showinfo("informacion", "empleado eliminado")
            actualizar()
        except Exception as e:
            print(e)
            mysqlC.rollback()
            mysqlC.close()

    def edit():
        nombreAdd = name.get()
        apellidoAdd = lastname.get()
        usuarioAdd = user.get()
        contraAdd = password.get()
        rolAdd = role_add.get()
        idAdd = identificador.get()
        
        if rolAdd == "":
            rolAdd = role.get()
        
        mysqlC = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "proyecto")
        micursos = mysqlC.cursor()
        try:
            micursos.execute(f"UPDATE usuarios set nombre = '{nombreAdd}', apellido = '{apellidoAdd}', usuario = '{usuarioAdd}', contraseña = '{contraAdd}', rol = '{rolAdd}' where id = {idAdd}")
            mysqlC.commit()
            name.delete(0, END)
            lastname.delete(0, END)
            user.delete(0, END)
            password.delete(0, END)
            role.delete(0, END)
            identificador.delete(0, END)
            messagebox.showinfo("informacion", "empleado editado")
            actualizar()
            
        except Exception as e:
            print(e)
            mysqlC.rollback()
            mysqlC.close()
        
    def obtenerR(event):
        name.delete(0, END)
        lastname.delete(0, END)
        user.delete(0, END)
        password.delete(0, END)
        role.delete(0, END)
        identificador.delete(0, END)
        
        renglon = listbox.selection()[0]
        print(renglon)
        seleccion = listbox.set(renglon)
        print(seleccion)
        identificador.insert(0, seleccion["Id"])
        name.insert(0, seleccion["Nombre"])
        lastname.insert(0, seleccion["Apellido"])
        user.insert(0, seleccion["Usuario"])
        password.insert(0, seleccion["Contraseña"])
        role.insert(0, seleccion["Rol"])
    
    def regresar():
        ventana_principal.destroy()
        mostrar_login()
    
    ventana_principal = tk.Tk()
    ventana_principal.geometry("1200x600")
    
    label1 = tk.Label(ventana_principal,text="Registro de empleados", fg="red",font=("Arial",28)).place(x=170,y=0)
    
    global name
    global lastname
    global user
    global password
    global role
    global identificador
    global role_add
    
    labelid = tk.Label(ventana_principal, text="ID", font=("Arial", 12))
    labelid.place(x=100, y=50)
    
    labelnombre = tk.Label(ventana_principal, text="Nombre", font=("Arial", 12))
    labelnombre.place(x=100, y=80)
    
    labelapellido = tk.Label(ventana_principal, text="Apellido", font=("Arial", 12))
    labelapellido.place(x=100, y=110)
    
    labelusuario = tk.Label(ventana_principal, text="Usuario", font=("Arial", 12))
    labelusuario.place(x=100, y=140)
    
    labelcontrasena = tk.Label(ventana_principal, text="Contraseña", font=("Arial", 12))
    labelcontrasena.place(x=100, y=170)
    
    labelrol = tk.Label(ventana_principal, text="Rol", font=("Arial", 12))
    labelrol.place(x=100, y=200)
    
    labelrol = tk.Label(ventana_principal, text="Agregar Rol", font=("Arial", 12))
    labelrol.place(x=400, y=170)
    
    identificador = tk.Entry(ventana_principal)
    identificador.place(x=270, y=50)
    
    name = tk.Entry(ventana_principal)
    name.place(x=270, y=80)
    
    lastname = tk.Entry(ventana_principal)
    lastname.place(x=270, y=110)
    
    user = tk.Entry(ventana_principal)
    user.place(x=270, y=140)
    
    password = tk.Entry(ventana_principal)
    password.place(x=270, y=170)
    
    role = tk.Entry(ventana_principal)
    role.place(x=270, y=200)
    
    role_add = ttk.Combobox(ventana_principal, values=["", "Empleado", "Administrador"], state="readonly")
    role_add.place(x=400, y=200)
    
    tk.Button(ventana_principal,text="Crear",command=add, height=5, width=10, font=("Arial",12)).place(x=100,y=230)
    tk.Button(ventana_principal,text="Editar",command=edit, height=5, width=10, font=("Arial",12)).place(x=250,y=230)
    tk.Button(ventana_principal,text="Eliminar",command=delete, height=5, width=10, font=("Arial",12)).place(x=400,y=230)
    tk.Button(ventana_principal,text="Regresar",command=regresar, height=5, width=10, font=("Arial",12)).place(x=550,y=230)
    
    columnas = ("Id","Nombre","Apellido","Usuario","Contraseña","Rol")
    listbox = ttk.Treeview(ventana_principal,columns=columnas,show="headings")
    
    for col in columnas:
        listbox.heading(col, text=col)
        listbox.grid(row=1, column=0, columnspan=1)
        listbox.place(x=0, y=350)
    
    mostrar()
    listbox.bind("<Double-Button-1>", obtenerR)
    
    ventana_principal.mainloop()

#! VENTANA DEL EMPLEADO

def mostrar_gestion_libros():
    ventana_sec = tk.Toplevel()
    ventana_sec.title("Gestion de Libros")
    ventana_sec.destroy()
    
    def mostrar():
        mysqlC = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "proyecto")
        micursos = mysqlC.cursor()
        micursos.execute("select * from libros")
        lista = micursos.fetchall() 
        
        for i,(id, titulo, autor, editorial, publicacion, precio) in enumerate(lista, start = 1):
            listbox.insert("", "end", values = (id, titulo, autor, editorial, publicacion, precio))
            mysqlC.close()

    def add():
        tituloAdd = title.get()
        autorAdd = writer.get()
        editorialAdd = editorial.get()
        publicacionAdd = publication.get()
        precioAdd = price.get()
        idAdd = identificador.get()
        mysqlC = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "proyecto")
        micursos = mysqlC.cursor()
        try:
            micursos.execute(f"insert into libros (id, titulo, autor, editorial, publicacion, precio) values('{idAdd}','{tituloAdd}','{autorAdd}','{editorialAdd}','{publicacionAdd}','{precioAdd}')")
            mysqlC.commit()
            title.delete(0, END)
            writer.delete(0, END)
            editorial.delete(0, END)
            publication.delete(0, END)
            price.delete(0, END)
            identificador.delete(0, END)
            messagebox.showinfo("informacion", "libro agregado")
            actualizar()
            
        except Exception as e:
            print(e)
            mysqlC.rollback()
            mysqlC.close()

    def actualizar():
        for i in listbox.get_children():
            listbox.delete(i)
        mostrar()
        
    def actualizar2():
        for i in listbox.get_children():
            listbox.delete(i)
 
    def delete():
        idAdd = identificador.get()
        mysqlC = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "proyecto")
        micursos = mysqlC.cursor()
        try:
            micursos.execute(f"DELETE FROM LIBROS WHERE id = {idAdd}")
            mysqlC.commit()
            title.delete(0, END)
            writer.delete(0, END)
            editorial.delete(0, END)
            publication.delete(0, END)
            price.delete(0, END)
            identificador.delete(0, END)
            messagebox.showinfo("informacion", "libro eliminado")
            actualizar()
        except Exception as e:
            print(e)
            mysqlC.rollback()
            mysqlC.close()

    def edit():
        tituloAdd = title.get()
        autorAdd = writer.get()
        editorialAdd = editorial.get()
        publicacionAdd = publication.get()
        precioAdd = price.get()
        idAdd = identificador.get()
        
        mysqlC = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "proyecto")
        micursos = mysqlC.cursor()
        try:
            micursos.execute(f"UPDATE libros set titulo = '{tituloAdd}', autor = '{autorAdd}', editorial = '{editorialAdd}', publicacion = '{publicacionAdd}', precio = '{precioAdd}' where id = {idAdd}")
            mysqlC.commit()
            title.delete(0, END)
            writer.delete(0, END)
            editorial.delete(0, END)
            publication.delete(0, END)
            price.delete(0, END)
            identificador.delete(0, END)
            messagebox.showinfo("informacion", "libro editado")
            actualizar()
            
        except Exception as e:
            print(e)
            mysqlC.rollback()
            mysqlC.close()
        
    def obtenerR(event):
        title.delete(0, END)
        writer.delete(0, END)
        editorial.delete(0, END)
        publication.delete(0, END)
        price.delete(0, END)
        identificador.delete(0, END)
        
        renglon = listbox.selection()[0]
        print(renglon)
        seleccion = listbox.set(renglon)
        print(seleccion)
        identificador.insert(0, seleccion["Id"])
        title.insert(0, seleccion["Titulo"])
        writer.insert(0, seleccion["Autor"])
        editorial.insert(0, seleccion["Editorial"])
        publication.insert(0, seleccion["Publicación"])
        price.insert(0, seleccion["Precio"])
    
    def filtrar_por_editorial():
        filtro_editorial = entry_editorial.get()
        
        mysqlC = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "proyecto")
        micursos = mysqlC.cursor()
        
        try:
            micursos.execute("SELECT DISTINCT editorial FROM libros")
            lista = [row[0] for row in micursos.fetchall()]

            if filtro_editorial not in lista:
                messagebox.showerror("Error", f"La editorial '{filtro_editorial}' no existe, vuelve a intentar")
                return

            micursos.execute("SELECT * FROM libros WHERE editorial = %s", (filtro_editorial,))
            lista = micursos.fetchall()
            actualizar2()

            if lista:
                for id, titulo, autor, editorial, publicacion, precio in lista:
                    listbox.insert("", "end", values=(id, titulo, autor, editorial, publicacion, precio))
                messagebox.showinfo("Información", "Datos filtrados correctamente.")
            else:
                messagebox.showinfo("Información", "No se encontraron libros con esa editorial")
        
        except Exception as e:
            print(e)
            mysqlC.rollback()
            mysqlC.close()
            
    def reiniciar():
        actualizar()
        messagebox.showinfo("Información", "Se ha quitado el filtro")
    
    def regresar():
        ventana_sec.destroy()
        mostrar_login()
    
    ventana_sec = tk.Tk()
    ventana_sec.geometry("1200x600")
    
    label1 = tk.Label(ventana_sec,text="Registro de libros", fg="red",font=("Arial",28)).place(x=170,y=0)
    
    global title
    global writer
    global editorial
    global publication
    global price
    global identificador
    
    labelid = tk.Label(ventana_sec, text="ID", font=("Arial", 12))
    labelid.place(x=100, y=50)
    
    labeltitulo = tk.Label(ventana_sec, text="Titulo", font=("Arial", 12))
    labeltitulo.place(x=100, y=80)
    
    labelautor = tk.Label(ventana_sec, text="Autor", font=("Arial", 12))
    labelautor.place(x=100, y=110)
    
    labeleditorial = tk.Label(ventana_sec, text="Editorial", font=("Arial", 12))
    labeleditorial.place(x=100, y=140)
    
    labelpublicacion = tk.Label(ventana_sec, text="Publicación", font=("Arial", 12))
    labelpublicacion.place(x=100, y=170)
    
    labelprecio = tk.Label(ventana_sec, text="Precio", font=("Arial", 12))
    labelprecio.place(x=100, y=200)
    
    labelfiltrareditorial = tk.Label(ventana_sec, text="Filtrar por Editorial", font=("Arial", 12))
    labelfiltrareditorial.place(x=400, y=170)
    
    identificador = tk.Entry(ventana_sec)
    identificador.place(x=270, y=50)
    
    title = tk.Entry(ventana_sec)
    title.place(x=270, y=80)
    
    writer = tk.Entry(ventana_sec)
    writer.place(x=270, y=110)
    
    editorial = tk.Entry(ventana_sec)
    editorial.place(x=270, y=140)
    
    publication = tk.Entry(ventana_sec)
    publication.place(x=270, y=170)
    
    price = tk.Entry(ventana_sec)
    price.place(x=270, y=200)
    
    entry_editorial = tk.Entry(ventana_sec)
    entry_editorial.place(x=400, y=200)
    
    tk.Button(ventana_sec,text="Crear",command=add, height=5, width=10, font=("Arial",12)).place(x=100,y=230)
    tk.Button(ventana_sec,text="Editar",command=edit, height=5, width=10, font=("Arial",12)).place(x=250,y=230)
    tk.Button(ventana_sec,text="Eliminar",command=delete, height=5, width=10, font=("Arial",12)).place(x=400,y=230)
    tk.Button(ventana_sec,text="Filtrar",command=filtrar_por_editorial, height=5, width=10, font=("Arial",12)).place(x=550,y=230)
    tk.Button(ventana_sec,text="Reiniciar",command=reiniciar, height=5, width=10, font=("Arial",12)).place(x=700,y=230)
    tk.Button(ventana_sec,text="Regresar",command=regresar, height=5, width=10, font=("Arial",12)).place(x=850,y=230)
    
    columnas = ("Id","Titulo","Autor","Editorial","Publicación","Precio")
    listbox = ttk.Treeview(ventana_sec,columns=columnas,show="headings")
    
    for col in columnas:
        listbox.heading(col, text=col)
        listbox.grid(row=1, column=0, columnspan=1)
        listbox.place(x=0, y=350)
    
    mostrar()
    listbox.bind("<Double-Button-1>", obtenerR)
    
    ventana_sec.mainloop()

#! LOGIN
def mostrar_login():
    root = tk.Tk()
    root.title("Login")
    root.geometry("300x200")
    
    label_usuario = tk.Label(root, text="Usuario:")
    label_usuario.pack(pady=5)
    entry_usuario = tk.Entry(root, width=30)
    entry_usuario.pack(pady=5)
    
    label_contraseña = tk.Label(root, text="Contraseña:")
    label_contraseña.pack(pady=5)
    entry_contraseña = tk.Entry(root, width=30, show="*")
    entry_contraseña.pack(pady=5)
    
    def verificar_usuario():
        usuario = entry_usuario.get()
        contraseña = entry_contraseña.get()
    
        try:
            conn = mysql.connector.connect(
                host='localhost',      
                user='root',          
                password='',  
                database='proyecto'    
                )
    
            cursor = conn.cursor()
    
            cursor.execute('''
                SELECT * FROM usuarios WHERE usuario = %s AND contraseña = %s
            ''', (usuario, contraseña))
    
            usuario = cursor.fetchone()
    
            if usuario:
                
                if usuario[5] == "Administrador":
                    messagebox.showinfo("Login exitoso", f"Bienvenido Administrador {usuario[1]}")
                    root.withdraw()
                    mostrar_gestion_empleados()
                    
                elif usuario[5] == "Empleado":
                    messagebox.showinfo("Login exitoso", f"Bienvenido Empleado {usuario[1]}")
                    root.withdraw()
                    mostrar_gestion_libros()
            else:
                messagebox.showerror("Error", "Usuario o contraseña no encontrados.")
    
        except mysql.connector.Error as err:
            messagebox.showerror("Error de conexión", f"Error: {err}")
    
        finally:
            if conn.is_connected():
                conn.close()  
    
    btn_login = tk.Button(root, text="Login", command=verificar_usuario)
    btn_login.pack(pady=20)
    
    root.mainloop()

mostrar_login()