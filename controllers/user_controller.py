from sqlalchemy.orm import Session

from models import UserManager, Role
from views.main_view import MainView
from views.user_view import UserView


class UserController:
    def __init__(self, user, db: Session):
        self.user_manager = UserManager()
        self.user = user
        self.db = db

    # USER MANAGEMENT MENU
    def user_management_menu(self):
        while True:
            choice = UserView.show_user_management_menu()
            match choice:
                case '1':
                    self.create_user()
                case '2':
                    self.update_user()
                case '3':
                    self.list_users()
                case '4':
                    self.delete_user()
                case 'b':
                    break
                case _:
                    MainView.print_invalid_input()

    def create_user(self):
        """Create a new user."""
        try:
            username, email, role, password = UserView.get_user_info()
            role_enum = Role[role.upper()]

            # Create user
            new_user = self.user_manager.add_user(username, email, role_enum, password)
            MainView.print_success(f"Utilisateur {new_user.username} créé avec succès. ID {new_user.id}.")
        except ValueError as ve:
            MainView.print_error(ve)
        except Exception as e:
            MainView.print_error(f"Erreur lors de la création de l'utilisateur : {e}")

    def list_users(self):
        """List all users - accessible to all users."""
        try:
            users = self.user_manager.get_all_users()
            if users:
                UserView.display_users_list(users)
            else:
                MainView.print_error("Aucun utilisateur trouvé.")
        except Exception as e:
            MainView.print_error(f"Erreur lors de la récupération des utilisateurs: {e}")

    def update_user(self):
        """Update an existing user."""
        user_id = UserView.get_user_id()

        existing_user = self.user_manager.get_user_by_id(user_id)
        if not existing_user:
            MainView.print_error(f"Utilisateur avec ID {user_id} introuvable.")
            return

        try:
            UserView.display_user_details(existing_user)
            updated_data = UserView.get_updated_user_data()

            updated_user = self.user_manager.update_user(user_id, updated_data)

            if updated_user:
                MainView.print_success("Les informations de l'utilisateur ont été mises à jour.")
                UserView.display_user_details(updated_user)
            else:
                MainView.print_error("Échec de la mise à jour de l'utilisateur.")
        except ValueError as e:
            MainView.print_error(f"Erreur lors de la mise à jour: {e}")
        except Exception as e:
            MainView.print_error(f"Une erreur inattendue est survenue: {e}")

    def delete_user(self):
        """Delete an existing user."""
        user_id = UserView.get_user_id()

        try:
            if self.user_manager.delete_user(user_id):
                MainView.print_success(f"L'utilisateur {user_id} a été supprimé avec succès.")
            else:
                MainView.print_error(f"L'utilisateur {user_id} n'a pas été trouvé.")
        except Exception as e:
            MainView.print_error(f"Erreur lors de la suppression de l'utilisateur: {e}")
