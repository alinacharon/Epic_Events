from sqlalchemy.orm import Session

from models import ContractManager, User, Role, Client
from views.contract_view import ContractView
from views.main_view import MainView


class ContractController:
    def __init__(self, user, db: Session):
        self.contract_manager = ContractManager()
        self.user = user
        self.db = db

    # MANAGEMENT TEAM
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
                    MainView.print_invalid_input()

    # COMMERCIAL TEAM MENU
    def commercial_contract_menu(self):
        """Contract management submenu for the Commercial role."""
        while True:
            contract_choice = ContractView.show_commercial_management_menu()
            match contract_choice:
                case "1":
                    self.list_all_contracts()
                case "2":
                    self.update_contract()
                case "3":
                    self.list_my_contracts()
                case "4":
                    self.show_unsigned_contracts()
                case "5":
                    self.show_not_fully_paid_contracts()
                case "b":
                    break
                case _:
                    MainView.print_invalid_input()

    def create_contract(self):
        """Creation of new contract"""
        try:
            contract_data = ContractView.get_contract_data()

            client_id = contract_data.get('client_id')
            client = self.db.query(Client).get(client_id)

            if not client:
                MainView.print_error(f"Client avec ID {client_id} n'existe pas.")
                return

            commercial_id = client.commercial_id

            commercial = self.db.query(User).get(commercial_id)
            if not commercial or commercial.role != Role.COMMERCIAL:
                MainView.print_error(f"L'utilisateur ID {commercial_id} n'est pas un commercial.")
                return

            contract_data['commercial_id'] = commercial_id

            new_contract = self.contract_manager.add_contract(contract_data)
            MainView.print_success(f"Nouveau contrat créé avec succès. ID: {new_contract.id}")
            return new_contract

        except ValueError as e:
            MainView.print_error(f"Erreur: {e} Veuillez réessayer.")
        except Exception as e:
            MainView.print_error(f"Une erreur inattendue est survenue: {e}")

    def list_all_contracts(self):
        """Retrieve and display all contracts - accessible to all users."""
        try:
            contracts = self.contract_manager.get_all_contracts()
            ContractView.display_contract_list(contracts)
        except Exception as e:
            MainView.print_error(f"Erreur lors de la récupération des contrats: {e}")

    def list_my_contracts(self):
        """List contracts associated with the current commercial."""
        if self.user.role != Role.COMMERCIAL:
            MainView.print_error("Accès refusé. Cette fonction est réservée aux commerciaux.")
            return
        try:
            contracts = self.contract_manager.get_contracts_by_commercial(self.user.id)
            ContractView.display_contract_list(contracts)
        except Exception as e:
            MainView.print_error(f"Erreur lors de la récupération de vos contrats: {e}")

    def update_contract(self):
        """Update an existing contract."""
        contract_id = ContractView.get_contract_id()
        existing_contract = self.contract_manager.get_contract_by_id(contract_id)

        if not existing_contract:
            MainView.print_error(f"Contrat avec l'ID {contract_id} introuvable.")
            return

        if self.user.role == Role.COMMERCIAL and existing_contract.commercial_id != self.user.id:
            MainView.print_error("Vous ne pouvez modifier que vos propres contrats.")
            return
        elif self.user.role == Role.SUPPORT:
            MainView.print_error("Vous n'avez pas les droits pour modifier les contrats.")
            return

        client_id = existing_contract.client_id
        client = self.db.query(Client).get(client_id)
        if not client:
            MainView.print_error(f"Client avec l'ID {client_id} introuvable.")
            return

        commercial_id = existing_contract.commercial_id
        commercial = self.db.query(User).get(commercial_id)
        if not commercial or commercial.role != Role.COMMERCIAL:
            MainView.print_error(f"L'utilisateur assigné avec l'ID {commercial_id} n'est pas un commercial.")
            return

        try:
            ContractView.display_contract_details(existing_contract)
            updated_data = ContractView.get_updated_contract_data()
            updated_contract = self.contract_manager.update_contract(contract_id, updated_data)

            if updated_contract:
                MainView.print_success("Les informations du contrat ont été mises à jour avec succès.")
            else:
                MainView.print_error("Échec de la mise à jour du contrat.")
        except ValueError as e:
            MainView.print_error(f"Erreur lors de la mise à jour: {e}")
        except Exception as e:
            MainView.print_error(f"Une erreur inattendue est survenue: {e}")

    def show_unsigned_contracts(self):
        """Display unsigned contracts."""
        try:
            unsigned_contracts = self.contract_manager.get_unsigned_contracts()
            ContractView.display_contract_list(unsigned_contracts)
        except Exception as e:
            MainView.print_error(f"Erreur lors de la récupération des contrats non signés: {e}")

    def show_not_fully_paid_contracts(self):
        """Display contracts that are not fully paid."""
        try:
            not_fully_paid_contracts = self.contract_manager.get_not_fully_paid_contracts()
            ContractView.display_contract_list(not_fully_paid_contracts)
        except Exception as e:
            MainView.print_error(f"Erreur lors de la récupération des contrats non totalement payés: {e}")
