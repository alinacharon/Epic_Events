from sqlalchemy.orm import sessionmaker
from controllers.user_controller import UserController
from controllers.main_controller import MainController
from config import engine
from database import init_database
import logging
from views.main_view import MainView

# Logging settings
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_app():
    """DB inisialization"""
    try:
        init_database()
        logger.info("Database initialized successfully")
    except Exception as e:
        logger.error(f"Failed to initialize database: {e}")
        raise


def get_db():
    """Session from DB"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def main():
    init_app()

    # Session generation
    db_generator = get_db()
    db = next(db_generator)

    try:
        user_controller = UserController(db)

        while True:
            print("\n1. Connexion")
            print("q. Quitter")
            choice = input("Choisissez une action : ")
            match choice:

                case '1':
                    # Login
                    username = input("Entrez le nom d'utilisateur : ")
                    # Запрос пароля
                    password = input("Entrez le mot de passe : ")
                    user = user_controller.login(
                        username, password)  # Используем метод login
                    if user:
                        MainView.print_success("Connexion réussie !")
                        open_main_menu(user, db)
                    else:
                        logger.warning(
                            f"Failed login attempt for username: {username}")
                        MainView.print_error(
                            "Utilisateur non trouvé ou mot de passe incorrect.")

                case 'q':
                    MainView.print_exit()
                    break

                case _:
                    MainView.print_invalid_input()
                    continue

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        print("Une erreur s'est produite. Veuillez réessayer plus tard.")

    finally:
        next(db_generator, None)  # Session closure


def open_main_menu(user, db):
    try:
        app = MainController(user, db)
        app.main_menu(user.role)
    except Exception as e:
        logger.error(f"Error in main menu: {e}")
        print("Une erreur s'est produite dans le menu principal.")


if __name__ == "__main__":
    main()
