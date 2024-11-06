class MainView:
    @staticmethod
    def print_success(info):
        print(f"\n\x1b[32m{info}\x1b[0m")

    @staticmethod
    def print_invalid_input():
        print("\n\x1b[33mInvalid input. Please enter a valid choice or a valid name.\x1b[0m")

    @staticmethod
    def print_error(info):
        print(f"\n\x1b[33m{info}\x1b[0m")

    @staticmethod
    def print_exit():
        print("\n\x1b[34mExiting program. Goodbye!\x1b[0m\n")

    @staticmethod
    def print_info(info):
        print(info)

    @classmethod
    def show_management_menu(cls):
        print("\nMenu Administrateur:")
        print("1. Gestion des utilisateurs")
        print("q. Quitter")
        choice = input("Enter your choice: ")
        return choice
