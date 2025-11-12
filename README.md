🏭 Sistema de Gestión de Piezas - Heineken
📋 Sistema completo de gestión de inventario de piezas desarrollado para Heineken, que permite registrar, consultar, actualizar y eliminar piezas con soporte para imágenes y búsqueda avanzada.

🚀 Tecnologías Utilizadas
Backend
Python 3.x - Lenguaje principal

SQLite - Base de datos embebida

SQL - Consultas y gestión de datos

Frontend
Tkinter - Interfaz gráfica de usuario

PIL (Pillow) - Procesamiento de imágenes

ttk - Widgets temáticos modernos

Arquitectura
Patrón MVC - Separación de concerns

CRUD Completo - Create, Read, Update, Delete

Manejo de BLOB - Almacenamiento de imágenes en BD

🛠️ Configuración e Instalación
Prerrequisitos
Bash

# Instalar dependencias
pip install pillow
Estructura de Archivos
Plaintext

ProyectoPiezas/
├── main.py              # Aplicación principal
├── PiezasDatos.py       # Lógica de negocio y CRUD
├── conexion.py          # Gestión de conexión a BD
└── Piezas.db            # Base de datos (se crea automáticamente)
Configuración de Base de Datos
La ruta de la base de datos es personalizable.

Python

# En conexion.py - RUTA PERSONALIZABLE
conexion = sqlite3.connect(r"\\LEONARDOFRANCO\PiezasDB\Piezas.db")

# Para cambiar la ubicación, modifica esta línea:
conexion = sqlite3.connect("ruta/personalizada/Piezas.db")
📖 Manual de Usuario
1. 🆕 Agregar Nueva Pieza
Pasos:

Completar campos obligatorios:

ID Pieza - Identificador único (requerido)

Línea - Línea de producción

Equipo - Equipo/Máquina asociada

Tipo - Tipo de pieza

Cantidad - Stock disponible (numérico)

Boquilla - Especificación técnica

Material - Material de fabricación

Agregar imágenes (opcional):

Click en "Agregar imagen" debajo de cada preview.

Formatos soportados: JPG, PNG, BMP, GIF.

Máximo 3 imágenes por pieza.

Guardar:

Click en botón "Agregar".

Recibirás una confirmación de éxito.

2. 🔍 Consultar Pieza Existente
Métodos de consulta:

A. Por ID específico:

Ingresar ID Pieza en campo superior.

Click en "Consultar".

El sistema carga automáticamente todos los datos y las vistas previas de las imágenes.

B. Búsqueda por filtros:

Seleccionar criterio: Línea, Equipo, Tipo o Material.

Ingresar texto a buscar.

Click en "Buscar".

Los resultados se filtrarán en la tabla.

C. Selección desde tabla:

Click en cualquier registro de la tabla "Piezas Registradas".

Los datos se cargan automáticamente en el formulario.

3. ✏️ Actualizar Pieza
Proceso:

Primero consultar la pieza a modificar (usando cualquiera de los métodos anteriores).

Realizar los cambios necesarios en los campos de texto.

Reemplazar imágenes si es necesario usando "Agregar imagen".

Click en "Actualizar".

Confirmar los cambios.

4. 🗑️ Eliminar Pieza
Proceso seguro:

Consultar la pieza que deseas eliminar.

Click en "Eliminar".

Aparecerá una confirmación de seguridad.

Click en "Yes" para confirmar la eliminación permanente.

5. 🖼️ Gestión de Imágenes
El sistema permite una gestión visual completa de las imágenes de las piezas.

Funcionalidades:

Vista previa de miniaturas (120x120px) en la pantalla principal.

Vista completa con información contextual al hacer clic en "Ver".

Múltiples formatos soportados.

Almacenamiento directo en la base de datos (BLOB).

Para ver imagen completa:

Cargar una pieza que contenga imágenes.

El botón "Ver" se habilitará automáticamente.

Click en "Ver" para abrir la ventana de visualización ampliada (como se muestra en la imagen).

🔧 Características Técnicas
Base de Datos
Esquema principal de la tabla piezas.

SQL

CREATE TABLE piezas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_pieza TEXT NOT NULL UNIQUE,
    linea TEXT NOT NULL,
    equipo TEXT NOT NULL,
    tipo TEXT NOT NULL,
    cantidad INTEGER NOT NULL,
    boquilla TEXT NOT NULL,
    material TEXT NOT NULL,
    imagen1 BLOB,
    imagen2 BLOB,
    imagen3 BLOB
);
Validaciones Implementadas
✅ ID Pieza único y obligatorio. ✅ Cantidad debe ser un valor numérico. ✅ Prevención de duplicados al registrar. ✅ Manejo de errores de conexión a la base de datos. ✅ Validación de formatos de imagen al cargar.

Búsqueda y Filtrado
🔍 Búsqueda en tiempo real en la tabla. 📊 Filtrado por múltiples criterios (Línea, Equipo, Tipo, Material). 🔄 Botón "Mostrar Todos" para resetear la vista de la tabla.

🎯 Flujo de Trabajo Recomendado
Plaintext

Para Nuevos Registros:
Ingresar ID → Completar datos → Agregar imágenes → Guardar
Plaintext

Para Modificaciones:
Consultar (por ID o tabla) → Verificar datos → Modificar campos → Actualizar
Plaintext

Para Eliminación:
Consultar (por ID o tabla) → Verificar pieza → Eliminar → Confirmar
⚠️ Solución de Problemas
Error: "Ya existe una pieza con el mismo ID"

Solución: Utilizar un ID Pieza diferente que sea único.

Error: "El campo Cantidad debe ser numérico"

Solución: Ingresar solo números en el campo Cantidad.

Error: "No se pudo cargar la imagen"

Solución: Verificar que el formato del archivo sea uno de los soportados (JPG, PNG, BMP, GIF) y que el archivo no esté corrupto.

Error de conexión a base de datos

Solución: Verificar que la ruta en conexion.py sea accesible, especialmente si es una unidad de red.

Python

# Verificar esta ruta en conexion.py
conexion = sqlite3.connect(r"\\LEONARDOFRANCO\PiezasDB\Piezas.db")
📞 Soporte
Versión: 1.0

Desarrollador: Leonardo Franco Pérez

Empresa: Heineken

Acceso a Información:

Menú Archivo → Versión - Muestra información de desarrollo.

Menú Archivo → Salir - Cierra la aplicación de forma segura.

🔄 Mantenimiento
Limpieza Regular: Usar el botón "Limpiar Campos" para resetear el formulario y comenzar un nuevo registro.

Backup de Datos: Se recomienda realizar una copia de seguridad regular del archivo Piezas.db, que se encuentra en la ruta configurada en conexion.py.

✅ Estado del Proyecto
[x] CRUD Completo - Funcional

[x] Gestión de Imágenes - Operativo

[x] Búsqueda Avanzada - Implementada

[x] Validaciones - Completas

[x] Interfaz de Usuario - Optimizada

[x] Manejo de Errores - Robustecido
