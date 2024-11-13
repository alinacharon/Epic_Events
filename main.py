import logging
import sentry_sdk
from sqlalchemy.orm import sessionmaker
from config import engine
from controllers.main_controller import MainController
from database import init_database
from views.main_view import MainView

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
# logging.disable(logging.CRITICAL)

# Создаем фабрику сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_app():
    """Инициализация базы данных"""
    try:
        init_database()
        logger.info("Database initialized successfully")
    except Exception as e:
        logger.error(f"Failed to initialize database: {e}")
        raise


def get_db():
    """Создаем сессию из БД"""
    db = SessionLocal()
    try:
        return db
    except Exception as e:
        logger.error(f"Error while creating session: {e}")
        raise
    finally:
        db.close()


def main():
    init_app()
    sentry_sdk.capture_message("Проверка подключения Sentry!")

    db = get_db()  # Получаем сессию

    try:
        main_controller = MainController(user=None, db=db) 
        user = None  

        while user is None:  
            choice = MainView.show_login_page() 
            if choice == '1':
                username, password = MainView.get_user_login_info()  
                user = main_controller.login(username, password)  
                if user:
                    MainView.print_success("Connexion réussie !")
                    main_controller.user = user  
                    main_controller.main_menu(user)
                else:
                    MainView.print_error("Utilisateur non trouvé ou mot de passe incorrect.")
            elif choice == 'q':
                MainView.print_exit()
                quit()
            else:
                MainView.print_invalid_input()

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        print("Une erreur s'est produite. Veuillez réessayer plus tard.")

    finally:
        if db:
            db.close()


if __name__ == "__main__":
    main()
