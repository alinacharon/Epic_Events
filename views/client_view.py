from rich.console import Console
from rich.table import Table
from rich import box
class ClientView:
    console = Console()
    
    @staticmethod
    def manage_clients_menu():
        """Displays the client management menu and returns the user's choice."""
        print("\nMenu de gestion des clients:")
        print("1. Créer un nouveau client")
        print("2. Voir la liste de tous les clients")
        print("3. Voir mes clients")
        print("4. Trouver un client")
        print("5. Modifier les informations d'un client")
        print("b. Retour au menu principal")
        print("q. Quitter")
        return input("Choisissez une option : ").strip()

    @staticmethod
    def get_client_data():
        """Get information about a client and return it as a dictionary."""
        print("\nEntrez les informations du nouveau client :")
        full_name = input("Nom complet : ").strip()
        email = input("Adresse e-mail : ").strip()
        phone = input("Téléphone : ").strip()
        company_name = input("Nom de l'entreprise : ").strip()

        return full_name, email, phone, company_name

    @staticmethod
    def display_client_list(client_list):
        """Displays a list of clients using Rich table."""
        ClientView.console.print("\n[bold cyan]Liste des clients :[/bold cyan]\n")

        if not client_list:
            ClientView.console.print("[bold red]Aucun client trouvé.[/bold red]")
            return

        table = Table(show_header=True, header_style="cyan", box=box.SQUARE)
        table.add_column("ID", style="dim", width=6)
        table.add_column("Nom du client", style="bold blue")
        table.add_column("Email", style="white")
        table.add_column("Entreprise", style="white")
        table.add_column("Téléphone", style="blue")
        table.add_column("Commercial", style="yellow")

        for client in client_list:
            commercial_username = client.commercial.username if client.commercial else "Non attribué"
            table.add_row(
                str(client.id),
                client.full_name,
                client.email,
                client.company_name if client.company_name else "N/A",
                client.phone if client.phone else "N/A",
                commercial_username
            )

        ClientView.console.print(table)

    @staticmethod
    def search_criteria():
        """Collects search criteria for finding clients."""
        print("\nEntrez les critères de recherche (laissez vide pour ignorer) :")
        full_name = input("Nom complet : ") or ""
        email = input("Adresse e-mail : ") or ""
        company_name = input("Nom de l'entreprise : ") or ""

        return {
            "full_name": full_name,
            "email": email,
            "company_name": company_name
        }

    @staticmethod
    def display_client_details(client):
        """Displays detailed information about a client."""
        print("\nInformations sur le client :")
        print(f"ID : {client.id}")
        print(f"Nom complet : {client.full_name}")
        print(f"Adresse e-mail : {client.email}")
        print(f"Téléphone : {client.phone}")
        print(f"Entreprise : {client.company_name}")
        print(f"Date de création : {client.created_at}")
        print(f"Dernière mise à jour : {client.updated_at}")
        print(f"Contact commercial : {client.commercial.username}")

    @staticmethod
    def get_client_id():
        """Prompts for the client ID to search or edit."""
        return input("Entrez l'ID du client : ").strip()

    @staticmethod
    def get_updated_client_data():
        """Collects updated data for editing a client."""
        print("\nEntrez les informations mises à jour (laissez vide pour conserver la valeur actuelle) :")
        full_name = input("Nom complet : ")
        email = input("Adresse e-mail : ")
        phone = input("Téléphone : ")
        company_name = input("Nom de l'entreprise : ")

        return {
            "full_name": full_name if full_name else None,
            "email": email if email else None,
            "phone": phone if phone else None,
            "company_name": company_name if company_name else None,
        }
