from sqlalchemy.orm import sessionmaker
from controllers.user_controller import UserController
from controllers.main_controller import MainController
from config import engine
from database import init_database
import logging
from views.main_view import MainView

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Создание фабрики сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_app():
    """Инициализация приложения и базы данных"""
    try:
        init_database()
        logger.info("Database initialized successfully")
    except Exception as e:
        logger.error(f"Failed to initialize database: {e}")
        raise

def get_db():
    """Функция для получения сессии базы данных"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def main():
    # Инициализация приложения
    init_app()

    # Создание генератора сессий
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
                    # Вход для существующего пользователя
                    username = input("Entrez le nom d'utilisateur : ")
                    password = input("Entrez le mot de passe : ")  # Запрос пароля
                    user = user_controller.login(username, password)  # Используем метод login
                    if user:
                        MainView.print_success("Connexion réussie !")
                        open_main_menu(user, db)
                    else:
                        logger.warning(f"Failed login attempt for username: {username}")
                        MainView.print_error("Utilisateur non trouvé ou mot de passe incorrect.")

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
        next(db_generator, None)  # Закрытие сессии

def open_main_menu(user, db):
    try:
        app = MainController(user, db)
        app.main_menu(user.role)
    except Exception as e:
        logger.error(f"Error in main menu: {e}")
        print("Une erreur s'est produite dans le menu principal.")

if __name__ == "__main__":
    main()