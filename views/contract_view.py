from models.entities.contract import Contract
from rich.console import Console
from rich.table import Table
from rich import box

class ContractView:
    console = Console()
    
    @classmethod
    def show_contract_management_menu(cls):
        """Display the contract management menu for management roles."""
        print("\nGestion des contrats:")
        print("1. Créer un nouveau contrat")
        print("2. Modifier un contrat existant")
        print("3. Voir tous les contrats")
        print("b. Retour")
        choice = input("Choisissez une option : ")
        return choice

    @classmethod
    def show_commercial_management_menu(cls):
        """Display the contract management menu for commercial roles."""
        print("\nGestion des contrats:\n")
        print("1. Voir tous les contrats")
        print("2. Mettre à jour les contrats de mes clients")
        print("3. Voir contrats de mes clients")
        print("4. Voir tous les contrats non signé")
        print("5. Voir tous les contrats non payés")
        print("b. Retour")
        choice = input("Choisissez une option : ")
        return choice
   
    @staticmethod
    def get_contract_id():
        """Get contract ID from user input."""
        while True:
            contract_id = input("Entrez le ID de contrat : ").strip()
            if not contract_id:  
                print("L'ID du contrat ne peut pas être vide. Veuillez entrer une valeur valide.")
                continue  
            return contract_id

    @classmethod
    def get_contract_data(cls):
        """Collect data for creating a new contract."""
        
        client_id = input("Entrez l'ID du client : ").strip()

        while True:
            total_amount_str = input("Entrez le montant total : ").strip()
            if not total_amount_str: 
                print("Le montant total ne peut pas être vide. Veuillez entrer une valeur valide.")
                continue
            try:
                total_amount = float(total_amount_str)
                break  
            except ValueError:
                print("Erreur: Veuillez entrer un montant valide sous forme de nombre.")

        while True:
            remaining_amount_str = input("Entrez le montant restant : ").strip()
            if not remaining_amount_str:  
                print("Le montant restant ne peut pas être vide. Veuillez entrer une valeur valide.")
                continue
            try:
                remaining_amount = float(remaining_amount_str)
                break  
            except ValueError:
                print("Erreur: Veuillez entrer un montant valide sous forme de nombre.")

        signed_input = input("Le contrat est-il signé ? (oui/non) : ").strip()
        signed = signed_input.lower() == 'oui'
        
        if not client_id or not signed_input:
            raise ValueError("Tous les champs sont obligatoire et ne peuvent pas être vides.")

        return {
            "client_id": client_id,
            "total_amount": total_amount,
            "remaining_amount": remaining_amount,
            "signed": signed
        }

    @staticmethod
    def display_contract_details(contract: 'Contract'):
        """Display detailed information about a contract."""
        print("\nInformations sur le contrat :")
        print(f"ID : {contract.id}")
        print(f"ID du client : {contract.client_id}")
        print(f"ID commercial : {contract.commercial_id}")
        print(f"Montant total : {contract.total_amount}")
        print(f"Montant restant : {contract.remaining_amount}")
        print(f"Contrat signé : {'Oui' if contract.signed else 'Non'}")

    @staticmethod
    def get_updated_contract_data():
        """Collect updated data for editing a contract."""
        print("\nEntrez les informations mises à jour (laissez vide pour conserver la valeur actuelle) :")
        total_amount = input("Montant total : ")
        remaining_amount = input("Montant restant : ")
        signed_input = input("Le contrat est-il signé ? (oui/non) : ")
        signed = signed_input.lower() == 'oui' if signed_input else None

        return {
            "total_amount": float(total_amount) if total_amount else None,
            "remaining_amount": float(remaining_amount) if remaining_amount else None,
            "signed": signed if signed_input else None
        }

    @staticmethod
    def display_contract_list(contracts):
        """Display a list of contracts using Rich table."""
        ContractView.console.print("\n[bold cyan]Liste des contrats :[/bold cyan]\n")

        if not contracts:
            ContractView.console.print("[bold red]Aucun contrat trouvé.[/bold red]")
            return

        table = Table(show_header=True, header_style="bold cyan", box=box.SQUARE)
        table.add_column("ID", style="dim", width=6)
        table.add_column("ID du client", style="bold blue")
        table.add_column("Commercial", style="white")
        table.add_column("Montant total", style="white")
        table.add_column("Montant restant", style="white")
        table.add_column("Signé", style="blue")

        for contract in contracts:
            client_id = str (contract.client_id )
            commercial_username = contract.commercial.username
            signed_status = "Oui" if contract.signed else "Non"
            
            table.add_row(
                str(contract.id),
                client_id,
                commercial_username,
                f"{contract.total_amount} €",
                f"{contract.remaining_amount} €",
                signed_status
            )

        ContractView.console.print(table)
