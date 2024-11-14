class UserView:

    @classmethod
    def show_user_management_menu(cls):
        print("\nGestion des employés:")
        print("1. Créer un nouvel employé")
        print("2. Mettre à jour les informations d'un employé")
        print("3. Liste des employés")
        print("4. Supprimer un employé")
        print("b. Retour")
        choice = input("Choisissez une option : ")
        return choice

    @staticmethod
    def get_user_id():
        """Prompts for the user ID to search or edit."""
        return input("Entrez le ID de employé : ").strip()

    @classmethod
    def get_user_info(cls):
        username = input("Entrez le nom d'utilisateur : ")
        email = input("Entrez l'adresse e-mail : ")
        role = input(
            "Entrez le rôle de l'utilisateur (COMMERCIAL, MANAGEMENT, SUPPORT) : ")
        password = input("Entrez le mot de passe : ")
        return username, email, role, password

    @staticmethod
    def display_user_details(user):
        """Displays detailed information about a user."""
        print("\nInformations sur le employé :")
        print(f"ID : {user.id}")
        print(f"Username: {user.username}")
        print(f"E-mail : {user.email}")
        print(f"Rôle : {user.role_value}")

    @staticmethod
    def get_updated_user_data():
        """Collects updated data for editing a user."""
        print("\nEntrez les informations mises à jour (laissez vide pour conserver la valeur actuelle) :")
        username = input("Nom d'utilisateur : ")
        email = input("Adresse e-mail : ")
        role = input("Rôle (COMMERCIAL, MANAGEMENT, SUPPORT) : ")

        # Return a dictionary with updated data or None if no new input is provided
        return {
            "username": username if username else None,
            "email": email if email else None,
            "role": role.upper() if role else None
        }
    @staticmethod
    def display_users_list(users):
        """Display a list of users."""
        if not users:
            print("Aucun utilisateur trouvé.")
        else:
            print("Liste des utilisateurs:")
            for user in users:
                print(f"ID: {user.id}, Nom: {user.username}, Email: {user.email}, Rôle: {user.role.name}")