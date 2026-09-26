import os
from modelos.usuario import Usuario
from modelos.producto import Producto
from servicios.archivo_servicio import ArchivoServicio

class RestauranteServicio:
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.ruta_usuarios = os.path.join(base_dir, "datos", "usuarios.json")
        self.ruta_productos = os.path.join(base_dir, "datos", "productos.json")
        
        self.usuarios = self._cargar_usuarios()
        self.productos = self._cargar_productos()

    def _cargar_usuarios(self) -> list:
        datos = ArchivoServicio.leer_json(self.ruta_usuarios)
        return [Usuario.from_dict(u) for u in datos]

    def _cargar_productos(self) -> list:
        datos = ArchivoServicio.leer_json(self.ruta_productos)
        return [Producto.from_dict(p) for p in datos]

    def _guardar_productos(self) -> bool:
        datos = [p.to_dict() for p in self.productos]
        return ArchivoServicio.guardar_json(self.ruta_productos, datos)

    def autenticar_usuario(self, username: str, password: str) -> Usuario | None:
        user_clean = username.strip().lower()
        pass_clean = password.strip()
        for u in self.usuarios:
            if u.username.strip().lower() == user_clean and str(u.password).strip() == pass_clean:
                return u
        return None

    def obtener_usuarios(self) -> list:
        return self.usuarios

    def obtener_productos(self) -> list:
        return self.productos

    def buscar_producto_por_id(self, id_producto: str) -> Producto | None:
        id_clean = id_producto.strip().lower()
        for p in self.productos:
            if p.id_producto.strip().lower() == id_clean:
                return p
        return None

    def registrar_producto(self, id_producto: str, nombre: str, precio: float, categoria: str, stock: int) -> tuple[bool, str]:
        if not id_producto or not nombre:
            return False, "El ID y el Nombre son obligatorios."
        if self.buscar_producto_por_id(id_producto):
            return False, "Ya existe un producto registrado con este ID."
        if precio <= 0:
            return False, "El precio debe ser un número mayor a cero."
        if stock < 0:
            return False, "El stock no puede ser negativo."

        nuevo_producto = Producto(id_producto.strip(), nombre.strip(), precio, categoria, stock)
        self.productos.append(nuevo_producto)
        if self._guardar_productos():
            return True, "Producto registrado correctamente."
        return False, "Error al guardar el producto en el archivo JSON."

    def actualizar_producto(self, id_producto: str, nombre: str, precio: float, categoria: str, stock: int) -> tuple[bool, str]:
        producto = self.buscar_producto_por_id(id_producto)
        if not producto:
            return False, "El producto especificado no existe."
        if not nombre:
            return False, "El campo Nombre no puede estar vacío."
        if precio <= 0 or stock < 0:
            return False, "Verifique que el precio sea mayor a 0 y el stock no sea negativo."

        producto.nombre = nombre.strip()
        producto.precio = precio
        producto.categoria = categoria
        producto.stock = stock

        if self._guardar_productos():
            return True, "Producto actualizado correctamente."
        return False, "Error al actualizar la información en el archivo JSON."

    def eliminar_producto(self, id_producto: str) -> tuple[bool, str]:
        producto = self.buscar_producto_por_id(id_producto)
        if not producto:
            return False, "El producto a eliminar no existe."

        self.productos.remove(producto)
        if self._guardar_productos():
            return True, "Producto eliminado correctamente."
        return False, "Error al guardar la eliminación en el archivo JSON."