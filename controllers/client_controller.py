from models.managers.client_manager import ClientManager
from models.entities.client import Client
from views.client_view import ClientView
from views.main_view import MainView


class ClientController:

    def __init__(self):
        database_url = "postgresql://admin:mypassword@localhost/database"
        self.client_manager = ClientManager(database_url)

    def client_menu(self):
        # Main client management menu loop
        while True:
            choice = ClientView.manage_clients_menu()
            match choice:
                case "1":
                    self.create_client()
                case "2":
                    self.list_all_clients()
                case "3":
                    self.search_clients()
                case "4":
                    self.update_client()
                case "b":
                    break
                case "q":
                    MainView.print_exit()
                    exit()
                case _:
                    MainView.print_invalid_input()
                    continue

    def create_client(self):
        try:
            client_data = ClientView.get_client_data()
            client = Client(**client_data)
            client.validate()
            new_client = self.client_manager.create_client(client_data)
            MainView.print_success("Nouveau client créé avec succès.")
            return new_client
        except ValueError as e:
            MainView.print_error(f"Erreur: {e} Veuillez réessayer.\n")
                
    def list_all_clients(self):
        # List all clients
        clients = self.client_manager.get_all_clients()
        ClientView.display_client_list(clients)

    def search_clients(self):
        # Search clients based on criteria
        search_criteria = ClientView.search_criteria()
        matched_clients = self.client_manager.search_clients(search_criteria)
        if matched_clients:
            ClientView.display_client_list(matched_clients)
        else:
            ClientView.print_error("Aucun client correspondant trouvé.")

    def update_client(self):
        client_id = ClientView.get_client_id()
        existing_client = self.client_manager.get_client_by_id(client_id)

        if existing_client:
            try:
                ClientView.display_client_details(existing_client)  
                updated_data = ClientView.get_updated_client_data()
                updated_client = self.client_manager.update_client(client_id, updated_data)

                if updated_client:
                    MainView.print_success("Les informations du client ont été mises à jour.")
                else:
                    MainView.print_error("Échec de la mise à jour du client.")
            except ValueError as e:
                MainView.print_error(f"Erreur lors de la mise à jour: {e}.")
            except Exception as e:
                MainView.print_error(f"Une erreur inattendue est survenue: {e}.")
        else:
            MainView.print_error(f"Client avec ID {client_id} introuvable.")
