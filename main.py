from tkinter import *
from tkinter import ttk
from tkinter import messagebox  
from tkinter import filedialog
from PIL import Image, ImageTk
import io
import PiezasDatos as crud

#ventana 
ventana = Tk()
ancho = 450
alto = 400
x_ventana = ventana.winfo_screenwidth() // 2 - ancho // 2
y_ventana = ventana.winfo_screenheight() // 2 - alto // 2
posicion = str(ancho) + "x" + str(alto) + "+" + str(x_ventana) + "+" + str(y_ventana)
ventana.geometry(posicion)
ventana.state('zoomed')
ventana.title("Piezas_Heineken")

#########Variables#####
txt_id_pieza=StringVar()
txt_linea=StringVar()
txt_equipo=StringVar()
txt_tipo=StringVar()
txt_cantidad=StringVar()
txt_boquilla=StringVar()
txt_material=StringVar()
txt_buscar=StringVar()
cbo_filtro=StringVar()
cbo_filtro.set("todos")

# Variables para imágenes
imagen1_data = None
imagen2_data = None
imagen3_data = None
imagen_labels = []

#####Funciones para imágenes######
def cargar_imagen(num_imagen):
    global imagen1_data, imagen2_data, imagen3_data
    
    file_path = filedialog.askopenfilename(
        title=f"Seleccionar Imagen {num_imagen}",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
    )
    
    if file_path:
        try:
            # Leer y redimensionar imagen
            imagen = Image.open(file_path)
            imagen = imagen.resize((120, 120), Image.Resampling.LANCZOS)
            foto = ImageTk.PhotoImage(imagen)
            
            # Guardar datos originales para la base de datos
            with open(file_path, 'rb') as file:
                imagen_data = file.read()
            
            # Actualizar la imagen correspondiente
            if num_imagen == 1:
                imagen1_data = imagen_data
                lbl_imagen1.config(image=foto, text="")
                lbl_imagen1.image = foto
                btn_ver1.config(state=NORMAL)
            elif num_imagen == 2:
                imagen2_data = imagen_data
                lbl_imagen2.config(image=foto, text="")
                lbl_imagen2.image = foto
                btn_ver2.config(state=NORMAL)
            elif num_imagen == 3:
                imagen3_data = imagen_data
                lbl_imagen3.config(image=foto, text="")
                lbl_imagen3.image = foto
                btn_ver3.config(state=NORMAL)
                
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar la imagen: {str(e)}")

def limpiar_imagen(num_imagen):
    global imagen1_data, imagen2_data, imagen3_data
    
    if num_imagen == 1:
        imagen1_data = None
        lbl_imagen1.config(image='', text="Imagen 1\nNo cargada", compound=TOP)
        btn_ver1.config(state=DISABLED)
    elif num_imagen == 2:
        imagen2_data = None
        lbl_imagen2.config(image='', text="Imagen 2\nNo cargada", compound=TOP)
        btn_ver2.config(state=DISABLED)
    elif num_imagen == 3:
        imagen3_data = None
        lbl_imagen3.config(image='', text="Imagen 3\nNo cargada", compound=TOP)
        btn_ver3.config(state=DISABLED)

def mostrar_imagen_grande(imagen_data, num_imagen):
    if imagen_data:
        try:
            # Crear ventana para mostrar imagen grande
            ventana_imagen = Toplevel(ventana)
            ventana_imagen.title(f"Imagen {num_imagen} - {txt_id_pieza.get()} - Vista Completa")
            ventana_imagen.geometry("700x650")
            ventana_imagen.configure(bg='white')
            
            # Frame para información
            info_frame = Frame(ventana_imagen, bg='white', padx=10, pady=10)
            info_frame.pack(fill=X)
            
            # Mostrar información de la pieza
            info_text = f"ID: {txt_id_pieza.get()} | Equipo: {txt_equipo.get()} | Tipo: {txt_tipo.get()}\n"
            info_text += f"Línea: {txt_linea.get()} | Material: {txt_material.get()} | Imagen: {num_imagen}"
            
            lbl_info = Label(info_frame, text=info_text, bg='white', font=("Verdana", 12, "bold"), 
                           justify=LEFT)
            lbl_info.pack(anchor=W)
            
            # Frame para la imagen
            img_frame = Frame(ventana_imagen, bg='white')
            img_frame.pack(expand=True, fill=BOTH, padx=10, pady=10)
            
            # Convertir datos de imagen
            imagen = Image.open(io.BytesIO(imagen_data))
            # Redimensionar manteniendo aspecto
            imagen.thumbnail((600, 500), Image.Resampling.LANCZOS)
            foto = ImageTk.PhotoImage(imagen)
            
            lbl_imagen_grande = Label(img_frame, image=foto, bg='white')
            lbl_imagen_grande.image = foto
            lbl_imagen_grande.pack(expand=True)
            
            # Botón para cerrar
            btn_cerrar = ttk.Button(ventana_imagen, text="Cerrar", command=ventana_imagen.destroy)
            btn_cerrar.pack(pady=10)
            
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo mostrar la imagen: {str(e)}")

#####Funciones existentes modificadas######
def creditos():
    messagebox.showinfo("Versión","Versión 1.0 \nDesarrollado por Leonardo Franco Pérez")

def salir():
    valor=messagebox.askquestion("Salir","¿Desea salir de la aplicación?")
    if valor=="yes":
        ventana.destroy()

def limpiar_campos():
    global imagen1_data, imagen2_data, imagen3_data
    
    txt_id_pieza.set("")
    txt_linea.set("")
    txt_equipo.set("")
    txt_tipo.set("")
    txt_cantidad.set("")
    txt_boquilla.set("")
    txt_material.set("")
    
    # Limpiar imágenes
    imagen1_data = None
    imagen2_data = None
    imagen3_data = None
    lbl_imagen1.config(image='', text="Imagen 1\nNo cargada", compound=TOP)
    lbl_imagen2.config(image='', text="Imagen 2\nNo cargada", compound=TOP)
    lbl_imagen3.config(image='', text="Imagen 3\nNo cargada", compound=TOP)
    btn_ver1.config(state=DISABLED)
    btn_ver2.config(state=DISABLED)
    btn_ver3.config(state=DISABLED)
    
    e_id_pieza.focus()

def llenar_tabla():
    tabla.delete(*tabla.get_children())
    res = crud.fiind_all()
    if res.get("respuesta"):
        piezas = res.get("piezas")
        for fila in piezas:
            tabla.insert("", END, values=fila)
    else:
        messagebox.showerror("Error", res.get("mensaje"))

def guardar():
    try:
        cantidad = int(txt_cantidad.get())
    except ValueError:
        messagebox.showwarning("Error","El campo 'Cantidad' debe ser numérico")
        txt_cantidad.set("")   
        e_cantidad.focus()
        return
    
    if not txt_id_pieza.get().strip():
        messagebox.showwarning("Error", "El campo 'ID Pieza' es obligatorio")
        e_id_pieza.focus()
        return
        
    pieza ={
        "id_pieza": txt_id_pieza.get(),
        "linea": txt_linea.get(),  # Ahora acepta texto y números
        "equipo": txt_equipo.get(),
        "tipo": txt_tipo.get(),
        "cantidad": cantidad,
        "boquilla": txt_boquilla.get(),
        "material": txt_material.get(),
        "imagen1": imagen1_data,
        "imagen2": imagen2_data,
        "imagen3": imagen3_data
    }
    
    res = crud.save(pieza)
    if res.get("respuesta"):
        llenar_tabla()
        messagebox.showinfo("OK", res.get("mensaje"))
        limpiar_campos()
    else:
        messagebox.showerror("Error", res.get("mensaje")) 

def consultar():
    if txt_id_pieza.get() != "":
        res = crud.find(txt_id_pieza.get())
        if res.get("respuesta"):
            pieza = res.get("pieza")
            if pieza:
                # Cargar datos básicos
                txt_id_pieza.set(pieza["id_pieza"])
                txt_linea.set(pieza["linea"])
                txt_equipo.set(pieza["equipo"])
                txt_tipo.set(pieza["tipo"])
                txt_cantidad.set(pieza["cantidad"])
                txt_boquilla.set(pieza["boquilla"])
                txt_material.set(pieza["material"])
                
                # Cargar imágenes si existen
                global imagen1_data, imagen2_data, imagen3_data
                imagen1_data = pieza.get("imagen1")
                imagen2_data = pieza.get("imagen2")
                imagen3_data = pieza.get("imagen3")
                
                # Mostrar miniaturas
                mostrar_miniatura(imagen1_data, lbl_imagen1, 1)
                mostrar_miniatura(imagen2_data, lbl_imagen2, 2)
                mostrar_miniatura(imagen3_data, lbl_imagen3, 3)
                
            else:
                e_id_pieza.focus()
                messagebox.showinfo("No encontrado", "No existe una pieza con ese ID")
                limpiar_campos()
        else:
            e_id_pieza.focus()
            limpiar_campos()
            messagebox.showerror("Error", res.get("mensaje"))
    else:
        messagebox.showwarning("Error", "Ingrese un ID de pieza para consultar")

def mostrar_miniatura(imagen_data, label_widget, num_imagen):
    if imagen_data:
        try:
            imagen = Image.open(io.BytesIO(imagen_data))
            imagen = imagen.resize((120, 120), Image.Resampling.LANCZOS)
            foto = ImageTk.PhotoImage(imagen)
            label_widget.config(image=foto, text="")
            label_widget.image = foto
            if num_imagen == 1:
                btn_ver1.config(state=NORMAL)
            elif num_imagen == 2:
                btn_ver2.config(state=NORMAL)
            elif num_imagen == 3:
                btn_ver3.config(state=NORMAL)
        except Exception as e:
            print(f"Error al mostrar miniatura: {e}")
    else:
        label_widget.config(image='', text=f"Imagen {num_imagen}\nNo cargada", compound=TOP)
        if num_imagen == 1:
            btn_ver1.config(state=DISABLED)
        elif num_imagen == 2:
            btn_ver2.config(state=DISABLED)
        elif num_imagen == 3:
            btn_ver3.config(state=DISABLED)

def actualizar():
    if not txt_id_pieza.get().strip():
        messagebox.showwarning("Error", "Primero debe consultar una pieza para actualizar")
        e_id_pieza.focus()
        return
    
    # QUITAMOS LA VALIDACIÓN NUMÉRICA PARA LÍNEA
    # Solo validamos que cantidad sea numérico
    try:
        cantidad = int(txt_cantidad.get())
    except ValueError:
        messagebox.showwarning("Error","El campo 'Cantidad' debe ser numérico")
        return
    
    pieza ={
        "id_pieza": txt_id_pieza.get(),
        "linea": txt_linea.get(),  # Ahora acepta texto y números
        "equipo": txt_equipo.get(),
        "tipo": txt_tipo.get(),
        "cantidad": cantidad,
        "boquilla": txt_boquilla.get(),
        "material": txt_material.get(),
        "imagen1": imagen1_data,
        "imagen2": imagen2_data,
        "imagen3": imagen3_data
    }
    
    res = crud.update(pieza)
    if res.get("respuesta"):
        llenar_tabla()
        messagebox.showinfo("OK", res.get("mensaje"))
        limpiar_campos()
    else:
        messagebox.showerror("Error", res.get("mensaje"))

def eliminar():
    if not txt_id_pieza.get().strip():
        messagebox.showwarning("Error", "Primero debe consultar una pieza para eliminar")
        e_id_pieza.focus()
        return
    
    valor = messagebox.askquestion("Eliminar", f"¿Está seguro de eliminar la pieza {txt_id_pieza.get()}?")
    if valor == "yes":
        res = crud.delete(txt_id_pieza.get())
        if res.get("respuesta"):
            llenar_tabla()
            messagebox.showinfo("OK", res.get("mensaje"))
            limpiar_campos()
        else:
            messagebox.showerror("Error", res.get("mensaje"))

def buscar_por_filtro():
    texto_buscar = txt_buscar.get().strip()
    filtro = cbo_filtro.get()
    
    tabla.delete(*tabla.get_children())
    
    if filtro == "todos" or not texto_buscar:
        llenar_tabla()
        return
    
    res = crud.fiind_all()
    if res.get("respuesta"):
        piezas = res.get("piezas")
        encontrados = 0
        
        for fila in piezas:
            if filtro == "linea":
                if texto_buscar.lower() in str(fila[1]).lower():  # Ahora busca texto también
                    tabla.insert("", END, values=fila)
                    encontrados += 1
            elif filtro == "equipo":
                if texto_buscar.lower() in fila[2].lower():
                    tabla.insert("", END, values=fila)
                    encontrados += 1
            elif filtro == "tipo":
                if texto_buscar.lower() in fila[3].lower():
                    tabla.insert("", END, values=fila)
                    encontrados += 1
            elif filtro == "material":
                if texto_buscar.lower() in fila[6].lower():
                    tabla.insert("", END, values=fila)
                    encontrados += 1
        
        if encontrados == 0:
            messagebox.showinfo("Búsqueda", "No se encontraron registros con los criterios especificados")
    else:
        messagebox.showerror("Error", res.get("mensaje"))

def seleccionar_fila(event):
    item = tabla.selection()
    if item:
        valores = tabla.item(item, "values")
        if valores:
            txt_id_pieza.set(valores[0])
            consultar()

#####Fin Funciones#####

####GUI######
fuente = ("Verdana", 11)

# Crear un frame principal para organizar mejor
main_frame = Frame(ventana, bg='white')
main_frame.pack(fill=BOTH, expand=True, padx=5, pady=5)

# Configurar grid para que la tabla ocupe más espacio
main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)
main_frame.rowconfigure(1, weight=3)

# Frame superior para formulario e imágenes
top_frame = Frame(main_frame, bg='white')
top_frame.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

# Frame para formulario (izquierda)
form_frame = Frame(top_frame, bg='white', relief=RAISED, bd=2)
form_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=(0, 5))

# Frame para imágenes (derecha)
imagenes_frame = Frame(top_frame, bg='white', relief=RAISED, bd=2)
imagenes_frame.pack(side=RIGHT, fill=BOTH, padx=(5, 0))

# Frame para tabla (ocupa toda la parte inferior)
table_frame = Frame(main_frame, bg='white')
table_frame.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)

# FORMULARIO (Todo en blanco)
form_inner_frame = Frame(form_frame, bg='white')
form_inner_frame.pack(fill=BOTH, expand=True, padx=15, pady=15)

# Título del formulario
Label(form_inner_frame, text="REGISTRO DE PIEZAS", bg='white', 
      font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=(0, 15))

# Etiquetas y campos del formulario
Label(form_inner_frame, text="ID Pieza:", anchor="w", justify="left", width=12, 
      bg="white", font=("Verdana", 12, "bold")).grid(row=1, column=0, padx=5, pady=8, sticky="w")
Label(form_inner_frame, text="Linea:", anchor="w", justify="left", width=12, 
      bg="white", font=("Verdana", 12)).grid(row=2, column=0, padx=5, pady=8, sticky="w")
Label(form_inner_frame, text="Equipo:", anchor="w", justify="left", width=12, 
      bg="white", font=("Verdana", 12)).grid(row=3, column=0, padx=5, pady=8, sticky="w")
Label(form_inner_frame, text="Tipo:", anchor="w", justify="left", width=12, 
      bg="white", font=("Verdana", 12)).grid(row=4, column=0, padx=5, pady=8, sticky="w")
Label(form_inner_frame, text="Cantidad:", anchor="w", justify="left", width=12, 
      bg="white", font=("Verdana", 12)).grid(row=5, column=0, padx=5, pady=8, sticky="w")
Label(form_inner_frame, text="Boquilla:", anchor="w", justify="left", width=12, 
      bg="white", font=("Verdana", 12)).grid(row=6, column=0, padx=5, pady=8, sticky="w")
Label(form_inner_frame, text="Material:", anchor="w", justify="left", width=12, 
      bg="white", font=("Verdana", 12)).grid(row=7, column=0, padx=5, pady=8, sticky="w")

###Inputs###
e_id_pieza = ttk.Entry(form_inner_frame, textvariable=txt_id_pieza, font=("Verdana", 12), width=20)
e_id_pieza.grid(row=1, column=1, padx=5, pady=8)
e_linea = ttk.Entry(form_inner_frame, textvariable=txt_linea, font=("Verdana", 12), width=20)
e_linea.grid(row=2, column=1, padx=5, pady=8)
e_equipo = ttk.Entry(form_inner_frame, textvariable=txt_equipo, font=("Verdana", 12), width=20)      
e_equipo.grid(row=3, column=1, padx=5, pady=8)
e_tipo = ttk.Entry(form_inner_frame, textvariable=txt_tipo, font=("Verdana", 12), width=20)
e_tipo.grid(row=4, column=1, padx=5, pady=8)  
e_cantidad = ttk.Entry(form_inner_frame, textvariable=txt_cantidad, font=("Verdana", 12), width=20)
e_cantidad.grid(row=5, column=1, padx=5, pady=8)
e_boquilla = ttk.Entry(form_inner_frame, textvariable=txt_boquilla, font=("Verdana", 12), width=20)
e_boquilla.grid(row=6, column=1, padx=5, pady=8)
e_material = ttk.Entry(form_inner_frame, textvariable=txt_material, font=("Verdana", 12), width=20)
e_material.grid(row=7, column=1, padx=5, pady=8)  
e_id_pieza.focus()

# Botones del formulario
botones_frame = Frame(form_inner_frame, bg='white')
botones_frame.grid(row=8, column=0, columnspan=2, pady=20)

ttk.Button(botones_frame, text="Agregar", command=guardar, width=12).pack(side=LEFT, padx=3)
ttk.Button(botones_frame, text="Consultar", command=consultar, width=12).pack(side=LEFT, padx=3)
ttk.Button(botones_frame, text="Actualizar", command=actualizar, width=12).pack(side=LEFT, padx=3)
ttk.Button(botones_frame, text="Eliminar", command=eliminar, width=12).pack(side=LEFT, padx=3)
ttk.Button(botones_frame, text="Limpiar", command=limpiar_campos, width=12).pack(side=LEFT, padx=3)

# IMÁGENES (Simple y en blanco)
imagenes_inner_frame = Frame(imagenes_frame, bg='white')
imagenes_inner_frame.pack(fill=BOTH, expand=True, padx=15, pady=15)

Label(imagenes_inner_frame, text="Visualización de Piezas ", bg='white', 
      font=("Arial", 14, "bold")).pack(pady=(0, 15))

# Frame para las imágenes en una sola fila
imagenes_row_frame = Frame(imagenes_inner_frame, bg='white')
imagenes_row_frame.pack(expand=True)

# Imagen 1
frame_imagen1 = Frame(imagenes_row_frame, bg='white')
frame_imagen1.pack(side=LEFT, padx=10)
lbl_imagen1 = Label(frame_imagen1, width=15, height=8, relief="solid", bg="white", bd=1,
                   text="Imagen 1\nNo cargada", font=("Verdana", 10), compound=TOP)
lbl_imagen1.pack(pady=5)
btn_agregar1 = ttk.Button(frame_imagen1, text="Agregar imagen", 
                         command=lambda: cargar_imagen(1), width=15)
btn_agregar1.pack(side=LEFT, padx=2)
btn_ver1 = ttk.Button(frame_imagen1, text="Ver", 
                     command=lambda: mostrar_imagen_grande(imagen1_data, 1), 
                     width=8, state=DISABLED)
btn_ver1.pack(side=LEFT, padx=2)

# Imagen 2
frame_imagen2 = Frame(imagenes_row_frame, bg='white')
frame_imagen2.pack(side=LEFT, padx=10)
lbl_imagen2 = Label(frame_imagen2, width=15, height=8, relief="solid", bg="white", bd=1,
                   text="Imagen 2\nNo cargada", font=("Verdana", 10), compound=TOP)
lbl_imagen2.pack(pady=5)
btn_agregar2 = ttk.Button(frame_imagen2, text="Agregar imagen", 
                         command=lambda: cargar_imagen(2), width=15)
btn_agregar2.pack(side=LEFT, padx=2)
btn_ver2 = ttk.Button(frame_imagen2, text="Ver", 
                     command=lambda: mostrar_imagen_grande(imagen2_data, 2), 
                     width=8, state=DISABLED)
btn_ver2.pack(side=LEFT, padx=2)

# Imagen 3
frame_imagen3 = Frame(imagenes_row_frame, bg='white')
frame_imagen3.pack(side=LEFT, padx=10)
lbl_imagen3 = Label(frame_imagen3, width=15, height=8, relief="solid", bg="white", bd=1,
                   text="Imagen 3\nNo cargada", font=("Verdana", 10), compound=TOP)
lbl_imagen3.pack(pady=5)
btn_agregar3 = ttk.Button(frame_imagen3, text="Agregar imagen", 
                         command=lambda: cargar_imagen(3), width=15)
btn_agregar3.pack(side=LEFT, padx=2)
btn_ver3 = ttk.Button(frame_imagen3, text="Ver", 
                     command=lambda: mostrar_imagen_grande(imagen3_data, 3), 
                     width=8, state=DISABLED)
btn_ver3.pack(side=LEFT, padx=2)

# BÚSQUEDA Y TABLA
search_frame = Frame(table_frame, bg="white", relief=RAISED, bd=1)
search_frame.pack(fill=X, pady=(0, 10))

Label(search_frame, text="Buscar por:", bg="white", font=("Verdana", 11)).pack(side=LEFT, padx=5)
combo_filtro = ttk.Combobox(search_frame, textvariable=cbo_filtro, 
                           values=["todos", "linea", "equipo", "tipo", "material"], 
                           state="readonly", width=12, font=("Verdana", 10))
combo_filtro.pack(side=LEFT, padx=5)

e_buscar = ttk.Entry(search_frame, textvariable=txt_buscar, font=("Verdana", 11), width=25)
e_buscar.pack(side=LEFT, padx=5)

ttk.Button(search_frame, text="Buscar", command=buscar_por_filtro).pack(side=LEFT, padx=5)
ttk.Button(search_frame, text="Mostrar Todos", command=llenar_tabla).pack(side=LEFT, padx=5)

# TABLA
titulo = Label(table_frame, text="Piezas Registradas", bg="white", 
               font=("Arial", 16, "bold"))
titulo.pack(pady=(0, 10))

# Frame para tabla con scrollbar
table_container = Frame(table_frame, bg='white')
table_container.pack(fill=BOTH, expand=True)

# Scrollbars
v_scrollbar = ttk.Scrollbar(table_container, orient=VERTICAL)
h_scrollbar = ttk.Scrollbar(table_container, orient=HORIZONTAL)

tabla = ttk.Treeview(table_container, 
                    columns=("ID", "LINEA", "MÁQUINA", "TIPO", "CANTIDAD", "BOQUILLA", "MATERIAL"),
                    yscrollcommand=v_scrollbar.set,
                    xscrollcommand=h_scrollbar.set,
                    height=18)

v_scrollbar.config(command=tabla.yview)
h_scrollbar.config(command=tabla.xview)

v_scrollbar.pack(side=RIGHT, fill=Y)
h_scrollbar.pack(side=BOTTOM, fill=X)
tabla.pack(side=LEFT, fill=BOTH, expand=True)

# Configurar columnas de la tabla
tabla.column("#0", width=0, stretch=NO)
tabla.column("ID", width=180, anchor=CENTER)
tabla.column("LINEA", width=120, anchor=CENTER)
tabla.column("MÁQUINA", width=220, anchor=CENTER)
tabla.column("TIPO", width=200, anchor=CENTER)   
tabla.column("CANTIDAD", width=120, anchor=CENTER)
tabla.column("BOQUILLA", width=200, anchor=CENTER)
tabla.column("MATERIAL", width=220, anchor=CENTER)

tabla.heading("#0", text="")
tabla.heading("ID", text="ID PIEZA")  
tabla.heading("LINEA", text="LÍNEA")
tabla.heading("MÁQUINA", text="EQUIPO/MÁQUINA")
tabla.heading("TIPO", text="TIPO")
tabla.heading("CANTIDAD", text="CANTIDAD")
tabla.heading("BOQUILLA", text="BOQUILLA")
tabla.heading("MATERIAL", text="MATERIAL")

# Vincular evento de selección
tabla.bind("<<TreeviewSelect>>", seleccionar_fila)

#####Menu#####
menuTop=Menu(ventana)
m_archivo=Menu(menuTop,tearoff=0)
m_archivo.add_command(label="Versión",command=creditos)
m_archivo.add_command(label="Salir",command=salir)
menuTop.add_cascade(label="Archivo", menu=m_archivo)  

m_limpiar=Menu(menuTop,tearoff=0)
m_limpiar.add_command(label="Limpiar Campos", command=limpiar_campos)
menuTop.add_cascade(label="Limpiar", menu=m_limpiar) 

m_crud=Menu(menuTop,tearoff=0)
m_crud.add_command(label="Guardar", command=guardar)
m_crud.add_command(label="Consultar", command=consultar)
m_crud.add_command(label="Actualizar", command=actualizar)
m_crud.add_command(label="Eliminar", command=eliminar)
menuTop.add_cascade(label="Pieza", menu=m_crud)

ventana.config(menu=menuTop)
llenar_tabla()
ventana.mainloop()