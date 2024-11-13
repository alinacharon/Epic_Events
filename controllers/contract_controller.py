from sqlalchemy.orm import Session

from models import ContractManager
from models import Role
from views.client_view import ClientView
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
                    print("Option invalide. Veuillez réessayer.")

    # COMMERCIAL TEAM MENU
    def commercial_contract_menu(self):
        """Contract management submenu for the Commercial role."""
        while True:
            contract_choice = ContractView.show_commercial_management_menu()
            match contract_choice:
                case "1":
                    self.list_all_contracts()
                case "2":
                    if self.user.role == Role.COMMERCIAL:
                        self.update_contract()
                    else:
                        MainView.print_error("Accès refusé. Seuls les commerciaux peuvent mettre à jour les contrats.")
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
                    session.commit()
                    MainView.print_success("Les informations du contract ont été mises à jour.")
                else:
                    MainView.print_error("Échec de la mise à jour du contract.")
            except ValueError as e:
                MainView.print_error(f"Erreur lors de la mise à jour: {e}")
            except Exception as e:
                MainView.print_error(f"Une erreur inattendue est survenue: {e}")


    def show_unsigned_contracts(self):
        """Display unsigned contracts."""
        unsigned_contracts = self.contract_manager.get_unsigned_contracts()
        if not unsigned_contracts:
            MainView.print_error("Aucun contrat non signé.")  # No unsigned contracts.
        else:
            MainView.print_info("Contrats non signés :")  # Unsigned contracts:
            for contract in unsigned_contracts:
                MainView.print_info(f"ID du contrat : {contract.id}, Montant total : {contract.total_amount}, Montant restant : {contract.remaining_amount}")

    def show_not_fully_paid_contracts(self):
        """Display contracts that are not fully paid."""
        not_fully_paid_contracts = self.contract_manager.get_not_fully_paid_contracts()
        if not not_fully_paid_contracts:
            MainView.print_error("Aucun contrat qui n'est pas entièrement payé.")  # No contracts that are not fully paid.
        else:
            MainView.print_info("Contrats qui ne sont pas entièrement payés :")  # Contracts that are not fully paid:
            for contract in not_fully_paid_contracts:
                MainView.print_info(f"ID du contrat : {contract.id}, Montant total : {contract.total_amount}, Montant restant : {contract.remaining_amount}")