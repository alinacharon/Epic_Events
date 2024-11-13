from controllers.client_controller import ClientController
from controllers.contract_controller import ContractController
from controllers.event_controller import EventController
from controllers.user_controller import UserController
from views.main_view import MainView
from models import User, UserManager

class MainController:
    def __init__(self, user, db):
        self.user = user
        self.db = db


    def login(self, username: str, password: str) -> User:
        try:
            user = self.db.query(User).filter(User.username == username).first()
            if user:
                user_manager = UserManager()  # Создаем экземпляр UserManager
                if user_manager.verify_password(password, user.password):  # Проверка пароля
                    MainView.print_info(f"L'utilisateur {username} s'est connecté avec succès.")
                    return user
                else:
                    MainView.print_error(f"Échec de la connexion pour l'utilisateur {username}.")

            return None
        except Exception as e:
            MainView.print_error(f"Erreur lors de la connexion : {e}")
            return None

    def open_main_menu(self, user):
        """Open the main menu for the logged-in user."""
        try:
            self.main_menu(user)
        except Exception as e:
            MainView.print_error(f"Une erreur s'est produite dans le menu principal: {e}")

    def main_menu(self, user):
        """Display the main menu based on the user's role."""
        role = user.role_value
        print(f"User role: {role}")

        if role == 'MANAGEMENT':
            self.show_management_menu()
        elif role == 'COMMERCIAL':
            self.show_commercial_menu()
        elif role == 'SUPPORT':
            self.show_support_menu()
        else:
            print("Rôle inconnu.")

    # MANAGEMENT TEAM MENU
    def show_management_menu(self):
        while True:
            choice = MainView.show_management_menu()
            match choice:
                case '1':
                    user_controller = UserController(self.user,self.db)
                    user_controller.user_management_menu()
                case '2':
                    contract_controller = ContractController(self.user, self.db)
                    contract_controller.contract_management_menu()
                case '3':
                    event_controller = EventController(self.user, self.db)
                    event_controller.event_management_menu()
                case '4':
                    client_controller = ClientController(self.user, self.db)
                    client_controller.list_all_clients()
                case 'q':
                    MainView.print_exit()
                    quit()
                case _:
                    MainView.print_invalid_input()
                    continue

    # COMMERCIAL TEAM MENU
    def show_commercial_menu(self):
        while True:
            choice = MainView.show_commercial_menu()
            match choice:
                case "1":
                    client_controller = ClientController(self.user, self.db)
                    client_controller.commercial_client_menu()
                case "2":
                    contract_controller = ContractController(self.user, self.db)
                    contract_controller.commercial_contract_menu()
                case "3":
                    event_controller = EventController(self.user, self.db)
                    event_controller.commercial_event_menu()
                case 'q':
                    MainView.print_exit()
                    quit()
                case _:
                    MainView.print_invalid_input()

    # SUPPORT TEAM MENU
    def show_support_menu(self):
        while True:
            choice = MainView.show_support_menu()
            match choice:
                case '1':
                    # Меню для управления событиями
                    event_controller = EventController(self.user, self.db)
                    event_controller.event_support_menu()
                case '2':
                    # Просмотр клиентов
                    client_controller = ClientController(self.user, self.db)
                    client_controller.view_clients()
                case '3':
                    # Просмотр контрактов
                    contract_controller = ContractController(self.user, self.db)
                    contract_controller.view_contracts()
                case 'q':
                    MainView.print_exit()
                    quit()
                case _:
                    MainView.print_invalid_input()
                    continue
