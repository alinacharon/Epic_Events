from controllers.client_controller import ClientController
from views.main_view import MainView
from views.user_view import UserView
from views.contract_view import ContractView

from controllers.user_controller import UserController
from controllers.contract_controller import ContractController

from models import User, Role



class MainController:
    def __init__(self, user, db):
        self.user = user
        self.db = db

    def main_menu(self, role):
        role = self.user.role_value
        print(f"User role: {role}")

        if role == 'MANAGEMENT':
            self.manage_management_menu()
        elif role == 'COMMERCIAL':
            self.show_commercial_menu()
        elif role == 'SUPPORT':
            self.show_support_menu()
        else:
            print("Rôle inconnu.")

    def manage_management_menu(self):
        while True:
            choice = MainView.show_management_menu()

            match choice:
                case '1':
                    user_controller = UserController(self.db) 
                    user_controller.user_management_menu()
                case '2':
                    contract_controller = ContractController(self.user,self.db) 
                    contract_controller.contract_management_menu()
                case '3':
                    pass
                case '4':
                    client_controller = ClientController(self.user,self.db) 
                    client_controller.list_all_clients()
                    
                case 'q':
                    break
                case _:
                    MainView.print_invalid_input()
                    continue

