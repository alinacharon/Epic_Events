from controllers.client_controller import ClientController
from views.main_view import MainView

from controllers.user_controller import UserController

from models.entities.user import Role



class MainController:
    def __init__(self, user, db):
        self.user = user
        self.db = db

    def main_menu(self, role):
        role = self.user.role  
        print(f"User role: {role}")

        if role == Role.ADMIN:
            self.manage_admin_menu()
        elif role == Role.MANAGEMENT:
            self.show_management_menu()
        elif role == Role.COMMERCIAL:
            self.show_commercial_menu()
        elif role == Role.SUPPORT:
            self.show_support_menu()
        else:
            print("Rôle inconnu.")

    def manage_admin_menu(self):
        while True:
            choice = MainView.show_admin_menu()

            match choice:
                case '1':
                    user_controller = UserController(self.db)
                    user_controller.user_management_menu()
                case 'q':
                    break
                case _:
                    MainView.print_invalid_input()
                    continue


    def system_settings_menu(self):
        # Здесь добавьте логику для управления системными настройками
        print("Gestion des paramètres du système...")

    def view_system_logs(self):
        # Здесь добавьте логику для просмотра системных логов
        print("Affichage des logs du système...")

    def all_roles_menu(self):
        while True:
            print("\nToutes les fonctions des autres rôles:")
            print("1. Fonctions de gestion")
            print("2. Fonctions commerciales")
            print("3. Fonctions de support")
            print("b. Retour")

            choice = input("Choisissez une option (1-4) : ")

            match choice:
                case '1':
                    self.show_management_menu()
                case '2':
                    self.show_commercial_menu()
                case '3':
                    self.show_support_menu()
                case '4':
                    break
                case _:
                    print("Option invalide. Veuillez réessayer.")
