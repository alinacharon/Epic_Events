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

    # MANAGEMENT MENU

    @classmethod
    def show_management_menu(cls):
        print("\nMenu Administrateur:\n")
        print("1. Gestion des employés")
        print("2. Gestion des contrats")
        print("3. Gestion des événements")
        print("4. Voir les clients")
        print("q. Quitter")
        choice = input("Enter your choice: ")
        return choice

    # COMMERCIAL MENU
    @classmethod
    def show_commercial_menu(cls):
        print("\nMenu Commercial:\n")
        print("1. Gestion des clients")
        print("2. Gestion des contracts")
        print("3. Gestion des événements")
        print("b. Retourner")
        print("q. Quitter")
        choice = input("Choisissez une option : ")
        return choice

    # SUPPORT MENU
    @classmethod
    def show_support_menu(cls):
        print("\nMenu Support:\n")
        print("1. Voir les événements assignés")
        print("2. Mettre à jour les informations des événements assignés")
        print(
            "3. Filtrer les événements (par exemple, uniquement ceux qui me sont assignés)")
        print("4. Voir les clients")
        print("5. Voir les contrats")
        print("q. Quitter")
        choice = input("Choisissez une option : ")
        return choice
