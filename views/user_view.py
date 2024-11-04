class UserView:
    @classmethod
    def user_management_menu(cls):
        print("\nGestion des utilisateurs:")
        print("1. Créer un nouvel utilisateur")
        print("2. Liste des utilisateurs")
        print("3. Supprimer un utilisateur")
        print("b. Retour")
        choice = input("Choisissez une option : ")
        return choice

    @classmethod
    def get_user_info(cls):
        username = input("Entrez le nom d'utilisateur : ")
        email = input("Entrez l'adresse e-mail : ")
        role = input("Entrez le rôle de l'utilisateur (ADMIN, COMMERCIAL, MANAGEMENT, SUPPORT) : ")
        password = input("Entrez le mot de passe : ")
        return username, email, role, password
