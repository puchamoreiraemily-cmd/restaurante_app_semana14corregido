import tkinter as tk
from tkinter import ttk, messagebox
from servicios.restaurante_servicio import RestauranteServicio

class MainView(tk.Tk):
    def __init__(self, servicio: RestauranteServicio, usuario_actual):
        super().__init__()
        self.servicio = servicio
        self.usuario_actual = usuario_actual

        self.title("Restaurante App - Sistema de Gestión (Semana 14)")
        self.geometry("900x620")
        self.minsize(850, 580)

        self._crear_interfaz()
        self._cargar_datos_iniciales()

    def _crear_interfaz(self):
        # Header de bienvenida y usuario activo
        frame_header = ttk.Frame(self, padding="10", relief=tk.RAISED)
        frame_header.pack(fill=tk.X, side=tk.TOP)

        lbl_bienvenida = ttk.Label(
            frame_header, 
            text=f"Usuario Activo: {self.usuario_actual.username} | Rol: {self.usuario_actual.rol}", 
            font=("Segoe UI", 10, "bold")
        )
        lbl_bienvenida.pack(side=tk.LEFT)

        btn_salir = ttk.Button(frame_header, text="Cerrar Sesión", command=self.destroy)
        btn_salir.pack(side=tk.RIGHT)

        # Contenedor Notebook (Pestañas)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.tab_productos = ttk.Frame(self.notebook, padding="10")
        self.tab_usuarios = ttk.Frame(self.notebook, padding="10")

        self.notebook.add(self.tab_productos, text="Gestión de Productos")
        self.notebook.add(self.tab_usuarios, text="Consulta de Usuarios")

        self._construir_pestana_productos()
        self._construir_pestana_usuarios()

    def _construir_pestana_productos(self):
        # Formulario con LabelFrame y Grid Layout
        frame_form = ttk.LabelFrame(self.tab_productos, text=" Formulario de Producto ", padding="10")
        frame_form.pack(fill=tk.X, side=tk.TOP, pady=(0, 10))

        frame_inputs = ttk.Frame(frame_form)
        frame_inputs.pack(fill=tk.X, expand=True)

        ttk.Label(frame_inputs, text="ID Producto:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.ent_id = ttk.Entry(frame_inputs, width=15)
        self.ent_id.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        ttk.Label(frame_inputs, text="Nombre:").grid(row=0, column=2, sticky=tk.W, padx=5, pady=5)
        self.ent_nombre = ttk.Entry(frame_inputs, width=25)
        self.ent_nombre.grid(row=0, column=3, sticky=tk.W, padx=5, pady=5)

        ttk.Label(frame_inputs, text="Categoría:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.cmb_categoria = ttk.Combobox(
            frame_inputs, 
            values=["Platos Fuertes", "Bebidas", "Postres", "Entradas"], 
            state="readonly", 
            width=13
        )
        self.cmb_categoria.current(0)
        self.cmb_categoria.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        ttk.Label(frame_inputs, text="Precio ($):").grid(row=1, column=2, sticky=tk.W, padx=5, pady=5)
        self.ent_precio = ttk.Entry(frame_inputs, width=12)
        self.ent_precio.grid(row=1, column=3, sticky=tk.W, padx=5, pady=5)

        ttk.Label(frame_inputs, text="Stock:").grid(row=1, column=4, sticky=tk.W, padx=5, pady=5)
        self.ent_stock = ttk.Entry(frame_inputs, width=10)
        self.ent_stock.grid(row=1, column=5, sticky=tk.W, padx=5, pady=5)

        # Botones de Acción
        frame_botones = ttk.Frame(frame_form, padding="5")
        frame_botones.pack(fill=tk.X, pady=(5, 0))

        ttk.Button(frame_botones, text="Registrar", command=self._accion_registrar).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_botones, text="Cargar/Consultar", command=self._accion_cargar).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_botones, text="Actualizar", command=self._accion_actualizar).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_botones, text="Eliminar", command=self._accion_eliminar).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_botones, text="Limpiar Campos", command=self._limpiar_formulario_productos).pack(side=tk.RIGHT, padx=5)

        # Tabla (Treeview) de productos
        frame_tabla = ttk.LabelFrame(self.tab_productos, text=" Catálogo de Productos ", padding="10")
        frame_tabla.pack(fill=tk.BOTH, expand=True)

        columnas = ("id", "nombre", "categoria", "precio", "stock")
        self.tree_productos = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=8)

        self.tree_productos.heading("id", text="ID")
        self.tree_productos.heading("nombre", text="Nombre")
        self.tree_productos.heading("categoria", text="Categoría")
        self.tree_productos.heading("precio", text="Precio ($)")
        self.tree_productos.heading("stock", text="Stock")

        self.tree_productos.column("id", width=90, anchor=tk.CENTER)
        self.tree_productos.column("nombre", width=240, anchor=tk.W)
        self.tree_productos.column("categoria", width=150, anchor=tk.W)
        self.tree_productos.column("precio", width=100, anchor=tk.E)
        self.tree_productos.column("stock", width=90, anchor=tk.CENTER)

        scrollbar_prod = ttk.Scrollbar(frame_tabla, orient=tk.VERTICAL, command=self.tree_productos.yview)
        self.tree_productos.configure(yscroll=scrollbar_prod.set)

        self.tree_productos.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar_prod.pack(side=tk.RIGHT, fill=tk.Y)

    def _construir_pestana_usuarios(self):
        frame_tabla_usr = ttk.LabelFrame(self.tab_usuarios, text=" Usuarios Registrados ", padding="10")
        frame_tabla_usr.pack(fill=tk.BOTH, expand=True)

        columnas = ("username", "rol")
        self.tree_usuarios = ttk.Treeview(frame_tabla_usr, columns=columnas, show="headings")

        self.tree_usuarios.heading("username", text="Nombre de Usuario")
        self.tree_usuarios.heading("rol", text="Rol Asignado")

        self.tree_usuarios.column("username", width=220, anchor=tk.W)
        self.tree_usuarios.column("rol", width=180, anchor=tk.CENTER)

        scrollbar_usr = ttk.Scrollbar(frame_tabla_usr, orient=tk.VERTICAL, command=self.tree_usuarios.yview)
        self.tree_usuarios.configure(yscroll=scrollbar_usr.set)

        self.tree_usuarios.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar_usr.pack(side=tk.RIGHT, fill=tk.Y)

    # Actualizaciones de la interfaz
    def _cargar_datos_iniciales(self):
        self._actualizar_tabla_productos()
        self._actualizar_tabla_usuarios()

    def _actualizar_tabla_productos(self):
        for item in self.tree_productos.get_children():
            self.tree_productos.delete(item)
        for p in self.servicio.obtener_productos():
            self.tree_productos.insert("", tk.END, values=(p.id_producto, p.nombre, p.categoria, f"{p.precio:.2f}", p.stock))

    def _actualizar_tabla_usuarios(self):
        for item in self.tree_usuarios.get_children():
            self.tree_usuarios.delete(item)
        for u in self.servicio.obtener_usuarios():
            self.tree_usuarios.insert("", tk.END, values=(u.username, u.rol))

    def _limpiar_formulario_productos(self):
        self.ent_id.delete(0, tk.END)
        self.ent_nombre.delete(0, tk.END)
        self.ent_precio.delete(0, tk.END)
        self.ent_stock.delete(0, tk.END)
        self.cmb_categoria.current(0)

    # Handlers conectados al servicio
    def _accion_registrar(self):
        try:
            id_prod = self.ent_id.get().strip()
            nom = self.ent_nombre.get().strip()
            cat = self.cmb_categoria.get()
            precio = float(self.ent_precio.get().strip())
            stock = int(self.ent_stock.get().strip())

            exito, msj = self.servicio.registrar_producto(id_prod, nom, precio, cat, stock)
            if exito:
                messagebox.showinfo("Registro Exitoso", msj)
                self._actualizar_tabla_productos()
                self._limpiar_formulario_productos()
            else:
                messagebox.showerror("Error de Registro", msj)
        except ValueError:
            messagebox.showerror("Error de Entrada", "Ingrese un precio numérico decimal válido y un stock entero.")

    def _accion_cargar(self):
        id_prod = self.ent_id.get().strip()
        if not id_prod:
            messagebox.showwarning("Atención", "Ingrese un ID de producto para realizar la búsqueda.")
            return

        producto = self.servicio.buscar_producto_por_id(id_prod)
        if producto:
            self.ent_nombre.delete(0, tk.END)
            self.ent_nombre.insert(0, producto.nombre)
            self.cmb_categoria.set(producto.categoria)
            self.ent_precio.delete(0, tk.END)
            self.ent_precio.insert(0, str(producto.precio))
            self.ent_stock.delete(0, tk.END)
            self.ent_stock.insert(0, str(producto.stock))
            messagebox.showinfo("Búsqueda Exitosa", f"Datos cargados para el producto con ID: {id_prod}")
        else:
            messagebox.showerror("No Encontrado", f"No se encontró un producto registrado con el ID '{id_prod}'.")

    def _accion_actualizar(self):
        try:
            id_prod = self.ent_id.get().strip()
            nom = self.ent_nombre.get().strip()
            cat = self.cmb_categoria.get()
            precio = float(self.ent_precio.get().strip())
            stock = int(self.ent_stock.get().strip())

            exito, msj = self.servicio.actualizar_producto(id_prod, nom, precio, cat, stock)
            if exito:
                messagebox.showinfo("Actualización Exitosa", msj)
                self._actualizar_tabla_productos()
                self._limpiar_formulario_productos()
            else:
                messagebox.showerror("Error al Actualizar", msj)
        except ValueError:
            messagebox.showerror("Error de Entrada", "Compruebe que el precio y el stock sean valores numéricos válidos.")

    def _accion_eliminar(self):
        id_prod = self.ent_id.get().strip()
        if not id_prod:
            messagebox.showwarning("Atención", "Ingrese el ID del producto que desea eliminar.")
            return

        confirmacion = messagebox.askyesno("Confirmar Eliminación", f"¿Está seguro de eliminar el producto '{id_prod}'?")
        if confirmacion:
            exito, msj = self.servicio.eliminar_producto(id_prod)
            if exito:
                messagebox.showinfo("Eliminación Exitosa", msj)
                self._actualizar_tabla_productos()
                self._limpiar_formulario_productos()
            else:
                messagebox.showerror("Error al Eliminar", msj)