from sqlalchemy.orm import Session
from models import User, Role
from views.user_view import UserView
from views.main_view import MainView
from models import UserManager

class UserController:
    def __init__(self, db: Session):
        self.db = db
        self.user_manager = UserManager() 

    def user_management_menu(self):
        while True:
            choice = UserView.user_management_menu()
            match choice:
                case '1':
                    self.create_user()
                case '2':
                    self.list_users()
                case '3':
                    self.delete_user()
                case 'b':
                    break
                case _:
                    print("Option invalide. Veuillez réessayer.")

    def create_user(self):
        username, email, role, password = UserView.get_user_info()
        try:
            role_enum = Role[role.upper()]  # Преобразование строки в enum Role
            new_user = self.user_manager.add_user(self.db, username, email, role_enum, password)  # Используем UserManager
            MainView.print_success(f"Utilisateur {new_user.username} créé avec succès.")
        except ValueError as ve:
            MainView.print_error(ve)  # Выводим сообщение об ошибке, если пользователь уже существует
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

    def delete_user(self):
        username = input("Entrez le nom d'utilisateur à supprimer : ")
        user = self.db.query(User).filter(User.username == username).first()
        if user:
            self.db.delete(user)
            self.db.commit()
            print(f"Utilisateur {username} supprimé avec succès.")
        else:
            print(f"Utilisateur {username} non trouvé.")
                    
    
    def get_user_by_username(self, username: str) -> User:
        try:
            return self.db.query(User).filter(User.username == username).first()
        except Exception as e:
            MainView.print_error(f"Erreur lors de la recherche de l'utilisateur : {e}")
            return None

    def login(self, username: str, password: str) -> User:
        try:
            user = self.db.query(User).filter(User.username == username).first()
            if user:
                MainView.print_info(f"L'utilisateur {username} s'est connecté avec succès.")
                return user
            else:
                MainView.print_error(f"Échec de la connexion pour l'utilisateur {username}.")
                return None
        except Exception as e:
            MainView.print_error(f"Erreur lors de la connexion : {e}")
            return None
    
    def get_user_by_username(self, username: str) -> User:
        try:
            return self.db.query(User).filter(User.username == username).first()
        except Exception as e:
            MainView.print_error(f"Erreur lors de la recherche de l'utilisateur : {e}")
            return None