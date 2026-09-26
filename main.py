from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView

def iniciar_aplicacion():
    # Instancia del servicio principal
    servicio = RestauranteServicio()

    def abrir_menu_principal(usuario):
        app_main = MainView(servicio, usuario)
        app_main.mainloop()

    login_app = LoginView(servicio, on_login_success=abrir_menu_principal)
    login_app.mainloop()

if __name__ == "__main__":
    iniciar_aplicacion()