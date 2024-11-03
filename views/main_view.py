class MainView:
    @staticmethod
    def print_success_action(info):
        print(f"\n\x1b[32m{info}\x1b[0m")

    @staticmethod
    def print_invalid_input():
        print("\n\x1b[33mInvalid input. Please enter a valid choice or a valid name.\x1b[0m")

    @staticmethod
    def print_error_action(info):
        print(f"\n\x1b[33m{info}\x1b[0m")

    @staticmethod
    def print_exit():
        print("\n\x1b[34mExiting program. Goodbye!\x1b[0m\n")

    @staticmethod
    def print_info(info):
        print(info)

    @classmethod
    def main_menu(cls):
        print("\n--- Epic Events menu ---\n")
        print("1. Gestion des clients")
        print("2. Gestion des contrats")
        print("3. Gestion des événements")
        print("4. Gestion des utilisateurs")
        print("5. Mon profil")
        print("q. Quit")
        choice = input("Enter your choice: ")
        return choice
    
    @staticmethod
    def print_success(message):
        """Displays a success message for an operation."""
        print(f"\nSuccès : {message}")

    @staticmethod
    def print_error(error):
        """Displays an error message."""
        print(f"\nErreur : {error}")
#MENU PRINCIPAL
# 1. Gestion des clients
#    - Créer un client
#    - Consulter la liste des clients
#    - Rechercher/Filtrer des clients
#    - Modifier un client

# 2. Gestion des contrats
#    - Créer un contrat
#    - Consulter la liste des contrats
#    - Filtrer les contrats
#      * Contrats non signés
#      * Contrats non entièrement payés
#    - Modifier un contrat

# 3. Gestion des événements
#    - Créer un événement
#    - Consulter la liste des événements
#    - Filtres des événements
#      * Événements sans support attribué
#      * Mes événements (selon le rôle)
#    - Modifier un événement

# 4. Gestion des utilisateurs (pour l'équipe de gestion)
#    - Créer un collaborateur
#    - Modifier/Supprimer un collaborateur

# 5. Mon profil
#    - Consulter mes informations
#    - Modifier mon mot de passe

# 6. Déconnexion