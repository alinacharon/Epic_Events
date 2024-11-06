from models import Client, Role
from models import ClientManager
from views.client_view import ClientView
from views.main_view import MainView


class ClientController:
    def __init__(self, user, db):
        self.client_manager = ClientManager()
        self.user = user
        self.db = db

    def client_menu(self):
        while True:
            choice = ClientView.manage_clients_menu()
            match choice:
                case "1":
                    if self.user.role == Role.COMMERCIAL:
                        self.create_client()
                    else:
                        MainView.print_error("Accès refusé. Seuls les commerciaux peuvent créer des clients.")
                case "2":
                    self.list_all_clients()
                case "3":
                    self.list_my_clients()
                case "4":
                    self.search_clients()
                case "5":
                    if self.user.role == Role.COMMERCIAL:
                        self.update_client()
                    else:
                        MainView.print_error("Accès refusé. Seuls les commerciaux peuvent modifier des clients.")
                case "6":
                    self.view_client_details()
                case "b":
                    break
                case "q":
                    MainView.print_exit()
                    exit()
                case _:
                    MainView.print_invalid_input()
                    continue

    def create_client(self):
        """Create a new client."""
        try:
            client_data = ClientView.get_client_data()
            client_data['commercial_id'] = self.user.id
            client = Client(**client_data)
            client.validate()
            new_client = self.client_manager.create_client(client_data)
            MainView.print_success(f"Nouveau client créé avec succès. ID: {new_client.id}")
            return new_client
        except ValueError as e:
            MainView.print_error(f"Erreur: {e} Veuillez réessayer.")

    def list_all_clients(self):
        """List all clients - accessible to all users."""
        try:
            clients = self.client_manager.get_all_clients()
            ClientView.display_client_list(clients)
        except Exception as e:
            MainView.print_error(f"Erreur lors de la récupération des clients: {e}")

    def list_my_clients(self):
        """List clients associated with the current commercial."""
        if self.user.role != Role.COMMERCIAL:
            MainView.print_error("Accès refusé. Cette fonction est réservée aux commerciaux.")
            return
        try:
            clients = self.client_manager.get_clients_by_commercial(self.user.id)
            ClientView.display_client_list(clients)
        except Exception as e:
            MainView.print_error(f"Erreur lors de la récupération de vos clients: {e}")

    def search_clients(self):
        """Search clients based on criteria."""
        try:
            search_criteria = ClientView.search_criteria()
            matched_clients = self.client_manager.search_clients(search_criteria)
            if matched_clients:
                ClientView.display_client_list(matched_clients)
            else:
                MainView.print_error("Aucun client correspondant trouvé.")
        except Exception as e:
            MainView.print_error(f"Erreur lors de la recherche: {e}")

    def update_client(self):
        """Update an existing client."""
        client_id = ClientView.get_client_id()
        existing_client = self.client_manager.get_client_by_id(client_id)

        if not existing_client:
            MainView.print_error(f"Client avec ID {client_id} introuvable.")
            return

        # Verify if the client belongs to the current commercial
        if existing_client.commercial_id != self.user.id:
            MainView.print_error("Vous ne pouvez modifier que vos propres clients.")
            return

        try:
            ClientView.display_client_details(existing_client)
            updated_data = ClientView.get_updated_client_data()
            updated_client = self.client_manager.update_client(client_id, updated_data)

            if updated_client:
                MainView.print_success("Les informations du client ont été mises à jour.")
                ClientView.display_client_details(updated_client)
            else:
                MainView.print_error("Échec de la mise à jour du client.")
        except ValueError as e:
            MainView.print_error(f"Erreur lors de la mise à jour: {e}")
        except Exception as e:
            MainView.print_error(f"Une erreur inattendue est survenue: {e}")

    def view_client_details(self):
        """View detailed information about a client - accessible to all users."""
        try:
            client_id = ClientView.get_client_id()
            client = self.client_manager.get_client_by_id(client_id)
            if client:
                ClientView.display_client_details(client)
            else:
                MainView.print_error(f"Client avec ID {client_id} introuvable.")
        except Exception as e:
            MainView.print_error(f"Erreur lors de la récupération des détails du client: {e}")
