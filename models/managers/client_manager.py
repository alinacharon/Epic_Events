from datetime import datetime

from sqlalchemy.orm import sessionmaker

from config import engine
from models import Client


class ClientManager:
    def __init__(self):
        self.Session = sessionmaker(bind=engine)

    def create_client(self, client_data):
        with self.Session() as session:
            existing_client = session.query(Client).filter_by(email=client_data["email"]).first()
            if existing_client:
                raise ValueError("Le champ 'email' est déjà utilisé par un autre client.")

            client = Client(**client_data)
            client.validate()
            session.add(client)
            session.commit()
            return client

    def get_all_clients(self):
        with self.Session() as session:
            return session.query(Client).all()

    def search_clients(self, search_criteria):
        with self.Session() as session:
            query = session.query(Client)
            if "full_name" in search_criteria:
                query = query.filter(Client.full_name.ilike(f"%{search_criteria['full_name']}%"))
            if "email" in search_criteria:
                query = query.filter(Client.email.ilike(f"%{search_criteria['email']}%"))
            if "company_name" in search_criteria:
                query = query.filter(Client.company_name.ilike(f"%{search_criteria['company_name']}%"))
            return query.all()

    def get_client_by_id(self, client_id):
        with self.Session() as session:
            return session.query(Client).get(client_id)

    def update_client(self, client_id, updated_data):
        with self.Session() as session:
            client = session.query(Client).get(client_id)
            if not client:
                return False

            for key, value in updated_data.items():
                if value is not None:
                    setattr(client, key, value)

            client.last_updated = datetime.now()
            session.commit()
            return True
