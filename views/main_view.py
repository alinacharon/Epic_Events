class MainView:
    @staticmethod
    def print_success(info):
        print(f"\n\x1b[32m{info}\x1b[0m")

    @staticmethod
    def print_invalid_input():
        print(
            "\n\x1b[33mInvalid input. Please enter a valid choice or a valid name.\x1b[0m")

    @staticmethod
    def print_error(info):
        print(f"\n\x1b[33m{info}\x1b[0m")

    @staticmethod
    def print_exit():
        print("\n\x1b[34mExiting program. Goodbye!\x1b[0m\n")

    @staticmethod
    def print_info(info):
        print(info)
        
# Menus depending on roles

    # MANAGEMENT

    @classmethod
    def show_management_menu(cls):
        print("\nMenu Administrateur:")
        print("1. Gestion des employés")
        print("2. Gestion des contrats")
        print("3. Gestion des événements")
        print("4. Voir les clients")
        print("q. Quitter")
        choice = input("Enter your choice: ")
        return choice

    # COMMERCIAL

    @classmethod
    def show_commercial_menu(cls):
        print("\nCommercial Menu:")
        print("q. Quitter")

    # SUPPORT

    @classmethod
    def show_support_menu(cls):
        print("\nSupport Menu:")
        print("q. Quitter")
  
