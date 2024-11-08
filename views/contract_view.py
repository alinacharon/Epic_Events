
# 2. Gestion des contrats
#    - Créer un nouveau contrat
#    - Modifier un contrat existant

from typing import Dict, Optional
from models.entities.contract import Contract


class ContractView:
    @classmethod
    def show_contract_management_menu(cls):
        print("\nGestion des contrats:")
        print("1. Créer un nouveau contrat")
        print("2. Modifier un contrat existant")
        print("3.Voir tous le contrats")
        print("b. Retour")
        choice = input("Choisissez une option : ")
        return choice

    @staticmethod
    def get_contract_id():
        """Prompts for the contract ID to search or edit."""
        return input("Entrez le ID de contract : ").strip()

    @classmethod
    def get_contract_data(cls):
        """Collects contract information from user input."""
        client_id = input("Entrez l'ID du client : ")
        commercial_id = input("Entrez l'ID commercial : ")
        total_amount = float(input("Entrez le montant total : "))
        remaining_amount = float(input("Entrez le montant restant : "))
        signed_input = input("Le contrat est-il signé ? (oui/non) : ")
        signed = signed_input.lower() == 'oui'  

        return {
        "client_id": client_id,
        "commercial_id": commercial_id,
        "total_amount": total_amount,
        "remaining_amount": remaining_amount,
        "signed": signed
    }
    
    @staticmethod
    def display_contract_details(contract: 'Contract') -> None:
        """Displays detailed information about a contract."""
        print("\nInformations sur le contrat :")
        print(f"ID : {contract.id}")
        print(f"ID du client : {contract.client_id}")
        print(f"ID commercial : {contract.commercial_id}")
        print(f"Montant total : {contract.total_amount}")
        print(f"Montant restant : {contract.remaining_amount}")
        print(f"Contrat signé : {'Oui' if contract.signed else 'Non'}")

    @staticmethod
    def get_updated_contract_data() -> Dict[str, Optional[str]]:
        """Collects updated data for editing a contract."""
        print("\nEntrez les informations mises à jour (laissez vide pour conserver la valeur actuelle) :")
        client_id = input("ID du client : ")
        commercial_id = input("ID commercial : ")
        total_amount = input("Montant total : ")
        remaining_amount = input("Montant restant : ")
        signed_input = input("Le contrat est-il signé ? (oui/non) : ")
        signed = signed_input.lower() == 'oui' if signed_input else None  # Преобразуем ввод в булевый тип

        # Return a dictionary with updated data or None if no new input is provided
        return {
            "client_id": client_id if client_id else None,
            "commercial_id": commercial_id if commercial_id else None,
            "total_amount": float(total_amount) if total_amount else None,
            "remaining_amount": float(remaining_amount) if remaining_amount else None,
            "signed": signed if signed_input else None
        }
        
    @staticmethod
    def display_contract_list(contracts):
        """Affiche la liste des contrats."""
        print("\nListe des contrats :")
        if not contracts:
            print("Aucun contrat trouvé.")
            return

        for contract in contracts:
            print(f"- ID : {contract.id}, Client : {contract.client_id}, Com. ID : {contract.commercial_id}, "
                f"Montant total : {contract.total_amount}, Restant : {contract.remaining_amount}, "
                f"Signé : {'Oui' if contract.signed else 'Non'}")