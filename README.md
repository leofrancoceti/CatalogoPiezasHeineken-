<h1 align="center"> Sistema de Gestión de Piezas - Heineken</h1>

<p align="center">
 <b>Sistema completo de gestión de inventario de piezas</b> desarrollado para <b>Heineken</b>, que permite registrar, consultar, actualizar y eliminar piezas con soporte para imágenes y búsqueda avanzada.
</p>

---

##  Tecnologías Utilizadas

### Backend
- **Python 3.x** → Lenguaje principal  
- **SQLite** → Base de datos embebida local  
- **SQL** → Consultas y gestión de datos  

### Frontend
- **Tkinter** → Interfaz gráfica de usuario (GUI)  
- **ttk** → Widgets temáticos modernos  
- **PIL (Pillow)** → Procesamiento y visualización de imágenes  

### Arquitectura
- **Patrón MVC** → Separación clara de lógica, vista y datos  
- **CRUD Completo** → Crear, Leer, Actualizar y Eliminar registros  
- **Manejo de BLOBs** → Almacenamiento binario de imágenes en la base de datos  

---

##  Instalación y Configuración

###  Prerrequisitos

Asegúrate de tener instalado **Python 3.x**.  
Luego, instala las dependencias necesarias ejecutando:
pip install pillow
##  Estructura del proyecto
- ** 📁 Sistema_Piezas_Heineken/
- ** ├── 📄 main.py                 # Archivo principal del programa
├── 📄 conexion.py             # Conexión y manejo de la base de datos
├── 📄 PiezasDatoa.py 
├── 📁 images/                 # Carpeta para imágenes predeterminadas
│   ├── default.png
│   └── logo_heineken.png
├── 📁 data/                   # Carpeta de base de datos SQLite
│   └── piezas.db
├── 📄 README.md               # Documentación del proyecto
└── 📄 requirements.txt        # Dependencias del proyecto

### Manual de Usuario
 1. Inicio del Sistema

Al abrir la aplicación, se mostrará la ventana principal con el logotipo de Heineken y un menú de opciones.

 2. Registrar una Nueva Pieza

Haz clic en “Agregar Pieza”.

Completa los campos:

Nombre de la pieza

Código o ID

Descripción

Cantidad disponible

Imagen (opcional)

Presiona “Guardar”.
La pieza será registrada y aparecerá en la tabla principal.

3. Consultar Piezas

En la parte superior, encontrarás una barra de búsqueda.

Escribe el nombre o código de la pieza para filtrar los resultados.

 4. Actualizar Datos

Selecciona una pieza de la lista.

Presiona “Editar”.

Modifica los datos necesarios.

Guarda los cambios con “Actualizar”.

 5. Eliminar Piezas

Selecciona la pieza que deseas eliminar.

Presiona “Eliminar”.

Confirma la acción.

 6. Visualizar Imagen

Al seleccionar una pieza, la imagen asociada se mostrará automáticamente.

Si no existe una imagen, se mostrará la predeterminada (default.png).

## Base de Datos

El sistema utiliza una base de datos SQLite localizada en data/piezas.db.

Estructura de la tabla:
Campo	Tipo	Descripción
id	INTEGER (PK)	Identificador único
nombre	TEXT	Nombre de la pieza
codigo	TEXT	Código interno
descripcion	TEXT	Descripción técnica
cantidad	INTEGER	Existencia actual
imagen	BLOB	Imagen en formato binario

 Todos los cambios (agregar, actualizar, eliminar) se guardan automáticamente.

## Funcionalidades Clave

- ** CRUD completo (crear, leer, actualizar, eliminar)
- ** Almacenamiento local (sin conexión requerida)
- ** Búsqueda dinámica por nombre o código
- ** Vista previa de imágenes
- ** Diseño profesional con ttk
- ** Compatible con Windows, macOS y Linux

###Autor

Leonardo Franco Pérez
📍 Guadalajara, Jalisco
🎓 Ingeniería Mecatrónica — CETI
📧 leofranco300@gmail.com

## Créditos

Proyecto desarrollado como parte de una colaboración académica con Heineken México, enfocado en la gestión y trazabilidad de piezas industriales.
El sistema fue diseñado para optimizar los procesos de inventario y mantenimiento interno.

<img width="1917" height="888" alt="image" src="https://github.com/user-attachments/assets/86b1e1ed-1da0-480c-9206-e6883c9f0653" />
<img width="1858" height="926" alt="image" src="https://github.com/user-attachments/assets/8075a1d0-fbeb-4fe0-a31e-b4ed0f7d350a" />

## Desarrollado en Guadalajara, Jalisco

