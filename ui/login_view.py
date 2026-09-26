import tkinter as tk
from tkinter import ttk, messagebox
from servicios.restaurante_servicio import RestauranteServicio

class LoginView(tk.Tk):
    def __init__(self, servicio: RestauranteServicio, on_login_success):
        super().__init__()
        self.servicio = servicio
        self.on_login_success = on_login_success

        self.title("Inicio de Sesión - Restaurante App")
        self.geometry("400x320")
        self.resizable(False, False)

        self._configurar_estilos()
        self._crear_componentes()

    def _configurar_estilos(self):
        self.style = ttk.Style()
        self.style.theme_use("clam")

    def _crear_componentes(self):
        container = ttk.Frame(self, padding="20")
        container.pack(fill=tk.BOTH, expand=True)

        lbl_titulo = ttk.Label(container, text="Acceso al Sistema", font=("Segoe UI", 16, "bold"))
        lbl_titulo.pack(pady=(0, 15))

        frame_form = ttk.LabelFrame(container, text=" Credenciales ", padding="15")
        frame_form.pack(fill=tk.X, pady=5)

        ttk.Label(frame_form, text="Usuario:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.txt_usuario = ttk.Entry(frame_form, width=25)
        self.txt_usuario.grid(row=0, column=1, pady=5, padx=5)

        ttk.Label(frame_form, text="Contraseña:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.txt_password = ttk.Entry(frame_form, show="*", width=25)
        self.txt_password.grid(row=1, column=1, pady=5, padx=5)

        btn_ingresar = ttk.Button(container, text="Ingresar", command=self._autenticar)
        btn_ingresar.pack(fill=tk.X, pady=(15, 0))

        self.bind('<Return>', lambda event: self._autenticar())

    def _autenticar(self):
        usuario_val = self.txt_usuario.get().strip()
        pass_val = self.txt_password.get().strip()

        if not usuario_val or not pass_val:
            messagebox.showwarning("Campos Vacíos", "Por favor ingrese su usuario y contraseña.")
            return

        usuario_autenticado = self.servicio.autenticar_usuario(usuario_val, pass_val)
        if usuario_autenticado:
            self.destroy()
            self.on_login_success(usuario_autenticado)
        else:
            messagebox.showerror("Error de Autenticación", "Usuario o contraseña incorrectos.")