from rich.console import Console
from rich.table import Table
from rich import box
class UserView:
    console = Console()

    @classmethod
    def show_user_management_menu(cls):
        """Display the user management menu options."""
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
        """Prompt for the user ID to search or edit."""
        return input("Entrez l'ID de employé : ").strip()

    @classmethod
    def get_user_info(cls):
        """Collect user information for creating a new user."""
        username = input("Entrez le nom d'utilisateur : ")
        email = input("Entrez l'adresse e-mail : ")
        role = input(
            "Entrez le rôle de l'utilisateur (COMMERCIAL, MANAGEMENT, SUPPORT) : ")
        password = input("Entrez le mot de passe : ")
        return username, email, role, password

    @staticmethod
    def display_user_details(user):
        """Display detailed information about a user."""
        print("\nInformations sur le employé :")
        print(f"ID : {user.id}")
        print(f"Username: {user.username}")
        print(f"E-mail : {user.email}")
        print(f"Rôle : {user.role_value}")

    @staticmethod
    def get_updated_user_data():
        """Collect updated data for editing a user."""
        print("\nEntrez les informations mises à jour (laissez vide pour conserver la valeur actuelle) :")
        username = input("Nom d'utilisateur : ")
        email = input("Adresse e-mail : ")
        role = input("Rôle (COMMERCIAL, MANAGEMENT, SUPPORT) : ")

        return {
            "username": username if username else None,
            "email": email if email else None,
            "role": role.upper() if role else None
        }

    @staticmethod
    def display_users_list(users):
        """Display a list of users using Rich table."""
        UserView.console.print("\n[bold cyan]Liste des utilisateurs :[/bold cyan]\n")

        if not users:
            UserView.console.print("[bold red]Aucun utilisateur trouvé.[/bold red]")
            return

        table = Table(show_header=True, header_style="bold cyan", box=box.SQUARE)
        table.add_column("ID", style="dim", width=6)
        table.add_column("Nom d'utilisateur", style="bold blue")
        table.add_column("Email", style="cyan")
        table.add_column("Rôle", style="blue")

        for user in users:
            table.add_row(
                str(user.id),
                user.username,
                user.email,
                user.role.name
            )

        UserView.console.print(table)
