import pwinput


class MainView:
    @staticmethod
    def print_success(info):
        """Print a success message in green."""
        print(f"\n\x1b[32m{info}\x1b[0m\n")

    @staticmethod
    def print_invalid_input():
        """Print an error message for invalid input."""
        print(
            "\n\x1b[33mInvalid input. Please enter a valid choice or a valid name.\x1b[0m")

    @staticmethod
    def print_error(info):
        """Print an error message in yellow."""
        print(f"\n\x1b[33m{info}\x1b[0m\n")

    @staticmethod
    def print_exit():
        """Print a message indicating the program is exiting."""
        print("\n\x1b[34mExiting program. Goodbye!\x1b[0m\n")

    @staticmethod
    def print_info(info):
        """Print general information."""
        print(f'\n{info}\n')

    # Connection menu
    @classmethod
    def show_login_page(cls):
        """Display the login options."""
        print(
            "\n\033[38;5;213mBienvenue à Epic Event ! Veuillez vous connecter.\n\033[0m\n")
        print("1. Connexion")
        print("q. Quitter\n")
        choice = input("Choisissez une action : ")
        return choice

    @classmethod
    def get_user_login_info(cls):
        """Get user login information (username and password)."""
        username = input("Entrez le nom d'utilisateur : ")
        password = pwinput.pwinput("Entrez le mot de passe : ", mask="*")
        return username, password

    # Menus depending on roles

    # MANAGEMENT MENU
    @classmethod
    def show_management_menu(cls):
        """Display the management menu options."""
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
        """Display the commercial menu options."""
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
        """Display the support menu options."""
        print("\nMenu Support:\n")
        print("1. Gestion des événements")
        print("2. Voir les clients")
        print("3. Voir les contrats")
        print("4. Quitter")
        choice = input("Choisissez une option : ")
        return choice
