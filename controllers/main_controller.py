from controllers.client_controller import ClientController
from controllers.contract_controller import ContractController
from controllers.event_controller import EventController
from controllers.user_controller import UserController
from views.main_view import MainView


class MainController:
    def __init__(self, user, db):
        self.user = user
        self.db = db

    def main_menu(self, role):
        role = self.user.role_value
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
                    user_controller = UserController(self.db)
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
                    break
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
                case "q":
                    MainView.print_exit()
                    break
                case _:
                    MainView.print_invalid_input()

    # SUPPORT TEAM MENU
    def show_support_menu(self):
        while True:
            choice = MainView.show_support_menu()
            match choice:
                case '1':
                    event_controller = EventController(self.user, self.db)
                    event_controller.event_support_menu()
                case '2':
                    event_controller = EventController(self.user, self.db)
                    event_controller.update_assigned_event_info()
                case '3':
                    event_controller = EventController(self.user, self.db)
                    event_controller.filter_assigned_events()
                case '4':
                    client_controller = ClientController(self.user, self.db)
                    client_controller.view_clients()
                case '5':
                    contract_controller = ContractController(self.user, self.db)
                    contract_controller.view_contracts()
                case 'q':
                    break
                case _:
                    MainView.print_invalid_input()
                    continue
