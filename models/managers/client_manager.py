from sqlalchemy.orm import sessionmaker, joinedload

from config import engine
from models import Client


class ClientManager:
    def __init__(self):
        self.Session = sessionmaker(bind=engine)

    def add_client(self, full_name, email, phone, company_name, commercial_id):
        """Create a new client."""
        with self.Session() as session:
            existing_client = session.query(
                Client).filter_by(email=email).first()
            if existing_client:
                raise ValueError(
                    "Le champ 'email' est déjà utilisé par un autre client.")

            client = Client(
                full_name=full_name,
                email=email,
                phone=phone,
                company_name=company_name,
                commercial_id=commercial_id
            )

            session.add(client)
            session.commit()

            session.refresh(client)
            return client

    def get_all_clients(self):
        """Get all clients"""
        with self.Session() as session:
            clients = session.query(Client).options(
                joinedload(Client.commercial)).all()
            return clients

    def get_my_clients(self, commercial_id):
        """Get clients associated with a specific commercial representative."""
        with self.Session() as session:
            clients = session.query(Client).options(joinedload(Client.commercial)) \
                .filter(Client.commercial_id == commercial_id).all()
            return clients

    def search_clients(self, search_criteria):
        with self.Session() as session:
            query = session.query(Client).options(joinedload(Client.commercial))

            if "full_name" in search_criteria:
                query = query.filter(Client.full_name.ilike(f"%{search_criteria['full_name']}%"))
            if "email" in search_criteria:
                query = query.filter(Client.email.ilike(f"%{search_criteria['email']}%"))
            if "company_name" in search_criteria:
                query = query.filter(Client.company_name.ilike(f"%{search_criteria['company_name']}%"))

            return query.all()

    def get_client_by_id(self, client_id):
        """Получить клиента по ID с загрузкой связанных данных."""
        with self.Session() as session:
            client = session.query(Client).options(joinedload(Client.commercial)).get(client_id)
            return client

    def update_client(self, client_id, updated_data):
        """Update client with his ID."""
        with self.Session() as session:
            client = session.query(Client).get(client_id)
            if not client:
                return None
                
            for key, value in updated_data.items():
                if value is not None:
                    setattr(client, key, value)
                    
            session.commit()
            return client
