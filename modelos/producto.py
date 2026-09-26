class Producto:
    def __init__(self, id_producto: str, nombre: str, precio: float, categoria: str, stock: int):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.stock = stock

    def to_dict(self) -> dict:
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "precio": self.precio,
            "categoria": self.categoria,
            "stock": self.stock
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id_producto=data.get("id_producto", ""),
            nombre=data.get("nombre", ""),
            precio=float(data.get("precio", 0.0)),
            categoria=data.get("categoria", "General"),
            stock=int(data.get("stock", 0))
        )