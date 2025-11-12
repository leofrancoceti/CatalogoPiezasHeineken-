🏭 Sistema de Gestión de Piezas - Heineken
📋 Descripción del Proyecto
Sistema completo de gestión de inventario de piezas desarrollado para Heineken, que permite registrar, consultar, actualizar y eliminar piezas con soporte para imágenes y búsqueda avanzada.

https://via.placeholder.com/800x400?text=Interfaz+Principal+del+Sistema

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
bash
# Instalar dependencias
pip install pillow
Estructura de Archivos
text
ProyectoPiezas/
├── main.py              # Aplicación principal
├── PiezasDatos.py       # Lógica de negocio y CRUD
├── conexion.py          # Gestión de conexión a BD
└── Piezas.db           # Base de datos (se crea automáticamente)
Configuración de Base de Datos
python
# En conexion.py - RUTA PERSONALIZABLE
conexion = sqlite3.connect(r"\\LEONARDOFRANCO\PiezasDB\Piezas.db")

# Para cambiar la ubicación, modifica esta línea:
conexion = sqlite3.connect("ruta/personalizada/Piezas.db")
📖 Manual de Usuario
1. 🆕 Agregar Nueva Pieza
https://via.placeholder.com/600x300?text=Formulario+de+Registro

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

Click en "Agregar imagen" debajo de cada preview

Formatos soportados: JPG, PNG, BMP, GIF

Máximo 3 imágenes por pieza

Guardar:

Click en botón "Agregar"

Confirmación de éxito

2. 🔍 Consultar Pieza Existente
https://via.placeholder.com/600x300?text=Consulta+de+Piezas

Métodos de consulta:

A. Por ID específico:

Ingresar ID Pieza en campo superior

Click en "Consultar"

Sistema carga automáticamente todos los datos

B. Búsqueda por filtros:

Seleccionar criterio: Línea, Equipo, Tipo o Material

Ingresar texto a buscar

Click en "Buscar"

Resultados filtrados en tabla

C. Selección desde tabla:

Click en cualquier registro de la tabla

Datos se cargan automáticamente

3. ✏️ Actualizar Pieza
https://via.placeholder.com/600x300?text=Actualizaci%C3%B3n+de+Datos

Proceso:

Primero consultar la pieza a modificar

Realizar cambios en campos necesarios

Reemplazar imágenes si es necesario

Click en "Actualizar"

Confirmar cambios

4. 🗑️ Eliminar Pieza
Proceso seguro:

Consultar pieza a eliminar

Click en "Eliminar"

Confirmación de seguridad aparece

Click "Yes" para confirmar eliminación

5. 🖼️ Gestión de Imágenes
https://via.placeholder.com/600x300?text=Gesti%C3%B3n+de+Im%C3%A1genes

Funcionalidades:

Vista previa de miniaturas (120x120px)

Vista completa con información contextual

Múltiples formatos soportados

Almacenamiento en base de datos

Para ver imagen completa:

Cargar imagen primero

Botón "Ver" se habilita automáticamente

Click para abrir ventana de visualización ampliada

🔧 Características Técnicas
Base de Datos
sql
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
)
Validaciones Implementadas
✅ ID Pieza único y obligatorio

✅ Cantidad debe ser numérica

✅ Prevención de duplicados

✅ Manejo de errores de conexión

✅ Validación de formatos de imagen

Búsqueda y Filtrado
🔍 Búsqueda en tiempo real

📊 Filtrado por múltiples criterios

🔄 "Mostrar Todos" para resetear vista

📱 Interfaz responsive

🎯 Flujo de Trabajo Recomendado
Para Nuevos Registros:
text
Ingresar ID → Completar datos → Agregar imágenes → Guardar
Para Modificaciones:
text
Consultar → Verificar datos → Modificar → Actualizar
Para Eliminación:
text
Consultar → Verificar → Eliminar → Confirmar
⚠️ Solución de Problemas
Error: "Ya existe una pieza con el mismo ID"
Solución: Utilizar un ID diferente único

Error: "El campo Cantidad debe ser numérico"
Solución: Ingresar solo números en campo cantidad

Error: "No se pudo cargar la imagen"
Solución: Verificar formato del archivo (JPG, PNG, BMP, GIF)

Error de conexión a base de datos
Solución: Verificar que la ruta de la BD sea accesible

python
# Verificar esta ruta en conexion.py
conexion = sqlite3.connect(r"\\LEONARDOFRANCO\PiezasDB\Piezas.db")
📞 Soporte
Información de Versión
Versión: 1.0

Desarrollador: Leonardo Franco Pérez

Empresa: Heineken

Acceso a Información
Menú Archivo → Versión - Información de desarrollo

Menú Archivo → Salir - Cerrar aplicación

🔄 Mantenimiento
Limpieza Regular
Usar "Limpiar Campos" para resetear formulario

"Mostrar Todos" para actualizar vista de tabla

Backup de Datos
Realizar copia regular del archivo Piezas.db

La base de datos se encuentra en la ruta configurada

