from sqlalchemy.orm import Session

from models import User, Role, UserManager
from views.main_view import MainView
from views.user_view import UserView


class UserController:
    def __init__(self, user, db: Session):
        self.user = user
        self.db = db
        self.user_manager = UserManager()

    # MANAGEMENT
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
        username, email, role, password = UserView.get_user_info()
        try:
            role_enum = Role[role.upper()]
            with self.db as session:  # Используем контекстный менеджер для управления сессией
                new_user = self.user_manager.add_user(session, username, email, role_enum, password)
                session.commit()  # Коммитим изменения после добавления пользователя
                MainView.print_success(f"Utilisateur {new_user.username} créé avec succès.")
        except ValueError as ve:
            MainView.print_error(ve)
        except Exception as e:
            MainView.print_error(f"Erreur lors de la création de l'utilisateur : {e}")

    def list_users(self):
        users = self.db.query(User).all()
        if users:
            print("\nListe des utilisateurs:")
            for user in users:
                print(f"ID: {user.id}, Nom: {user.username}, Email: {user.email}, Rôle: {user.role.name}")
        else:
            print("Aucun utilisateur trouvé.")

    def update_user(self):
        """Update an existing user."""
        user_id = UserView.get_user_id()
        existing_user = self.user_manager.get_user_by_id(user_id)

        if not existing_user:
            MainView.print_error(f"User avec ID {user_id} introuvable.")
            return

        try:
            UserView.display_user_details(existing_user)
            updated_data = UserView.get_updated_user_data()

            with self.db as session:  # Используем контекстный менеджер для управления сессией
                updated_user = self.user_manager.update_user(session, user_id, updated_data)

                if updated_user:
                    MainView.print_success("Les informations du user ont été mises à jour.")
                    UserView.display_user_details(updated_user)
                else:
                    MainView.print_error("Échec de la mise à jour du user.")
        except ValueError as e:
            MainView.print_error(f"Erreur lors de la mise à jour: {e}")
        except Exception as e:
            MainView.print_error(f"Une erreur inattendue est survenue: {e}")

    def delete_user(self):
        """Delete an existing user."""
        username = input("Entrez le nom d'employé à supprimer : ")

        with self.db as session:  # Используем контекстный менеджер для управления сессией
            user = session.query(User).filter(User.username == username).first()
            if user:
                session.delete(user)
                session.commit()
                MainView.print_success(f"Utilisateur {username} supprimé avec succès.")
            else:
                MainView.print_error(f"Utilisateur {username} non trouvé.")
