from controllers.client_controller import ClientController
from views.main_view import MainView


# from event_controller import EventController
# from user_controller import UserController
# from contract_controller import ContractController
# from views.main_view import MainView


class MainController:
    def __init__(self):
        self.client_controller = ClientController()
        # self.event_controller = EventController()
        # self.user_controller = UserController()
        # self.contract_controller = ContractController()

    def main_menu(self):
        while True:
            choice = MainView.main_menu()
            match choice:
                case "1":
                    self.client_controller.client_menu()
                case "2":
                    self.contract_controller.contract_menu()
                case "3":
                    self.event_controller.event_menu()
                case "4":
                    self.user_controller.user_menu()
                case "5":
                    self.profile_controller.profile_menu()
                case "q":
                    MainView.print_exit()
                    exit()
                case _:
                    MainView.print_invalid_input()
                    continue