# Interfaz Gráfica con Tkinter - restaurante_app (Semana 14)

## Tema
Implementación de componentes y contenedores avanzadas en Tkinter para el sistema de gestión del restaurante.

## Objetivo del Proyecto
Evolucionar la interfaz gráfica previa mediante contenedores estructurados y componentes interactivos para permitir el mantenimiento completo (CRUD) de productos y la consulta de usuarios. La vista (GUI) mantiene una separación estricta de responsabilidades, gestionando eventos mediante el uso de `command=`, mientras que la lógica de negocio, validaciones y persistencia JSON se delegan a `RestauranteServicio`.

## Flujo de Información
La interacción con la aplicación sigue un flujo unidireccional y desacoplado entre capas:
Acción del usuario (Botón GUI) -> Evento Tkinter (`command=`) -> Controlador de vista (`MainView`) -> Métodos de negocio (`RestauranteServicio`) -> Persistencia (`ArchivoServicio` / JSON) -> Actualización dinámica de la interfaz (`Treeview`).

## Organización de Capas

```text
restaurante_app_semana14/
├── datos/
│   ├── productos.json
│   └── usuarios.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── main.py
└── README.md


datos/: Almacena los archivos productos.json y usuarios.json con los registros persistentes del restaurante.

modelos/: Clases Producto y Usuario que definen la estructura del dominio y métodos de conversión de datos (to_dict).

servicios/:

ArchivoServicio: Encargado de la lectura y escritura segura de archivos JSON.

RestauranteServicio: Concentra la lógica de autenticación, validaciones de negocio y operaciones de consulta, registro, edición y eliminación de productos.

ui/: Módulos visuales desarrollados con Tkinter y ttk (LoginView para autenticación y MainView para la gestión general).

main.py: Punto de entrada que inicializa la ventana base, instancia los servicios y gestiona la transición entre pantallas.

Elementos de Tkinter Aplicados
Contenedores
tk.Tk / tk.Toplevel: Ventana base y ventanas secundarias de la aplicación.

ttk.Notebook: Pestañas superiores para organizar de manera independiente los módulos de "Gestión de Productos" y "Consulta de Usuarios".

ttk.PanedWindow: Contenedor con división reajustable para separar el panel del formulario a la izquierda y el panel de visualización a la derecha.

tk.Frame / ttk.LabelFrame: Estructuras visuales borderizadas para agrupar entradas de datos, botones de acción y tablas de consulta.

Componentes de Entrada y Visualización
tk.Entry: Campos de entrada para captura de credenciales y datos numéricos/textuales del formulario de productos.

ttk.Combobox: Menú desplegable para la selección estructurada de categorías de productos (Plato Fuerte, Bebidas, Postres, Entradas).

ttk.Button: Desencadenadores de operaciones CRUD e interacciones de usuario.

ttk.Treeview: Tablas estructuradas para la presentación interactiva de productos y usuarios.

ttk.Scrollbar: Barra de desplazamiento vertical acoplada a las tablas para facilitar la navegación por grandes volúmenes de registros.

messagebox: Diálogos emergentes para confirmaciones de eliminación, advertencias de validación y mensajes de éxito o error.

Gestores de Geometría Empleados
pack(): Utilizado para la organización de contenedores globales, barras de encabezado y pestañas del Notebook.

grid(): Empleado en los formularios de captura dentro de los LabelFrame para alinear formalmente etiquetas, campos de texto y botones en filas y columnas.

Se evita estrictamente mezclar pack() y grid() dentro de un mismo contenedor padre para garantizar la estabilidad visual de la interfaz.

Manejo de Eventos y CRUD de Productos
Las interacciones de la interfaz se coordinan únicamente mediante callbacks asociadas al parámetro command= de los botones:

Registrar: Captura los valores de los campos, invoca a RestauranteServicio para validar y guardar el nuevo producto, actualiza el Treeview y sincroniza en productos.json.

Cargar / Consultar: Toma el ID seleccionado o ingresado, recupera el objeto desde el servicio y puebla automáticamente los campos del formulario.

Actualizar: Modifica el registro seleccionado aplicando las validaciones de negocio a través del servicio y refresca la vista.

Eliminar: Solicita confirmación mediante messagebox y remueve el registro tanto de la tabla como del archivo JSON.

Limpiar: Restablece y vacía las entradas del formulario para nuevos registros.

Comportamiento del Sistema
El ciclo operativo comprende: Inicio de aplicación -> Pantalla de Inicio de Sesión (LoginView) -> Autenticación exitosa -> Panel Principal (MainView). Desde el panel principal, el usuario navega entre las pestañas Usuarios (solo lectura) y Productos (gestión interactiva), observando reflejado cualquier cambio de manera inmediata.

Persistencia de Datos
La persistencia es totalmente transparente para la capa visual. Toda actualización realizada sobre los productos se almacena de forma inmediata en el archivo datos/productos.json a través de los métodos de RestauranteServicio.

Requisitos de Entorno
Python 3.10 o superior.

Módulo tkinter habilitado (incluido por defecto en la instalación estándar de Python).

Modo de Uso
Para ejecutar la aplicación desde la terminal, ubícate en la raíz del proyecto y ejecuta:
cd restaurante_app_semana14
py main.py

Credenciales de Acceso
Usuario: emily

Contraseña: 123