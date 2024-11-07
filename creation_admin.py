from sqlalchemy.orm import Session
from models import Role
from models.managers.user_manager import UserManager
from config import engine


def create_admin_user():

    user_manager = UserManager()

    # Session creation
    with Session(engine) as session:
        try:
            # Admin creation
            admin_user = user_manager.add_user(
                db=session,
                username='admin',
                email='admin@epicevents.com',
                role=Role.MANAGEMENT,
                password='12345'
            )
            print("Admin created")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    create_admin_user()
