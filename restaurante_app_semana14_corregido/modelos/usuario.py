class Usuario:
    def __init__(self, username: str, password: str, rol: str = "Usuario"):
        self.username = username
        self.password = password
        self.rol = rol

    def to_dict(self) -> dict:
        return {
            "username": self.username,
            "password": self.password,
            "rol": self.rol
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            username=data.get("username", ""),
            password=data.get("password", ""),
            rol=data.get("rol", "Usuario")
        )