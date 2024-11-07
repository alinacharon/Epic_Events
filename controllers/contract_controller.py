# 2. Gestion des contrats
#    - Créer un nouveau contrat
#    - Modifier un contrat existant

from models import Contract, Role
from models import ContractManager
from views.contract_view import ContractView
from views.main_view import MainView
from sqlalchemy.orm import Session


class ContractController:
    def __init__(self, user, db: Session):
        self.contract_manager = ContractManager()
        self.user = user
        self.db = db

    def contract_management_menu(self):
        while True:
            choice = ContractView.show_contract_management_menu()
            match choice:
                case '1':
                    self.create_contract()
                case '2':
                    self.update_contract()
                case '3':
                    self.list_all_contracts()
                case 'b':
                    break
                case _:
                    print("Option invalide. Veuillez réessayer.")


    def create_contract(self):
        """Create a new contract."""
        try:
            contract_data = ContractView.get_contract_data()
            with self.db as session:
                new_contract = self.contract_manager.add_contract(contract_data, session)
                MainView.print_success(f"Nouveau contract créé avec succès. ID: {new_contract.id}")
                return new_contract
        except ValueError as e:
            MainView.print_error(f"Erreur: {e} Veuillez réessayer.")
        except Exception as e:
            MainView.print_error(f"Une erreur inattendue est survenue: {e}")

    def list_all_contracts(self):
        """List all contracts - accessible to all users."""
        try:
            contracts = self.contract_manager.get_all_contracts()
            ContractView.display_contract_list(contracts)
        except Exception as e:
            MainView.print_error(f"Erreur lors de la récupération des contracts: {e}")

    def list_my_contracts(self):
        """List contracts associated with the current commercial."""
        if self.user.role != Role.COMMERCIAL:
            MainView.print_error("Accès refusé. Cette fonction est réservée aux commerciaux.")
            return
        try:
            contracts = self.contract_manager.get_contracts_by_commercial(self.user.id)
            ContractView.display_contract_list(contracts)
        except Exception as e:
            MainView.print_error(f"Erreur lors de la récupération de vos contracts: {e}")

    def search_contracts(self):
        """Search contracts based on criteria."""
        try:
            search_criteria = ContractView.search_criteria()
            matched_contracts = self.contract_manager.search_contracts(search_criteria)
            if matched_contracts:
                ContractView.display_contract_list(matched_contracts)
            else:
                MainView.print_error("Aucun contract correspondant trouvé.")
        except Exception as e:
            MainView.print_error(f"Erreur lors de la recherche: {e}")

    def update_contract(self):
        """Update an existing contract."""
        contract_id = ContractView.get_contract_id()
        with self.db as session:
            existing_contract = self.contract_manager.get_contract_by_id(contract_id, session)

            if not existing_contract:
                MainView.print_error(f"Contract avec ID {contract_id} introuvable.")
                return

        # Verify if the contract belongs to the current commercial
            if existing_contract.commercial_id != self.user.id:
                MainView.print_error("Vous ne pouvez modifier que vos propres contracts.")
                return

            try:
                ContractView.display_contract_details(existing_contract)
                updated_data = ContractView.get_updated_contract_data()
                updated_contract = self.contract_manager.update_contract(contract_id, updated_data)

                if updated_contract:
                    MainView.print_success("Les informations du contract ont été mises à jour.")
                    ContractView.display_contract_details(updated_contract)
                else:
                    MainView.print_error("Échec de la mise à jour du contract.")
            except ValueError as e:
                MainView.print_error(f"Erreur lors de la mise à jour: {e}")
            except Exception as e:
                MainView.print_error(f"Une erreur inattendue est survenue: {e}")

    def view_contract_details(self):
        """View detailed information about a contract - accessible to all users."""
        try:
            contract_id = ContractView.get_contract_id()
            contract = self.contract_manager.get_contract_by_id(contract_id)
            if contract:
                ContractView.display_contract_details(contract)
            else:
                MainView.print_error(f"Contract avec ID {contract_id} introuvable.")
        except Exception as e:
            MainView.print_error(f"Erreur lors de la récupération des détails du contract: {e}")
