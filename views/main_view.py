import pwinput


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


    # Connection menu
    @classmethod
    def show_login_page(cls):
        print("\n1. Connexion")
        print("q. Quitter")
        choice = input("Choisissez une action : ")
        return choice

    @classmethod
    def get_user_login_info(cls):
        username = input("Entrez le nom d'utilisateur : ")
        password = pwinput.pwinput("Entrez le mot de passe : ", mask="*")
        return username, password
    # Menus depending on roles

    # MANAGEMENT MENU

    @classmethod
    def show_management_menu(cls):
        print("\nMenu Gestion :\n")
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
        print("q. Quitter")
        choice = input("Choisissez une option : ")
        return choice

    # SUPPORT MENU
    @classmethod
    def show_support_menu(cls):
        print("\nMenu Support:\n")
        print("1. Gestion des événements")
        print("2. Voir les clients")
        print("3. Voir les contrats")
        print("4. Quitter")
        choice = input("Choisissez une option : ")
        return choice
