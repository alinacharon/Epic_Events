from datetime import datetime

from sqlalchemy import select
from sqlalchemy.orm import Session, sessionmaker

from database import engine
from models.entities.client import Client,clients

from sqlalchemy import create_engine, MetaData

class ClientManager:
    def __init__(self, database_url):
        # Логика подключения к базе данных
        self.engine = create_engine(database_url)
        self.metadata = MetaData()
        self.metadata.reflect(bind=self.engine)

        if 'clients' in self.metadata.tables:
            self.client_table = self.metadata.tables['clients']
        else:
            raise ValueError("Table 'clients' not found.")

        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def create_client(self, client_data):
        # Проверка на уникальность email
        existing_client = self.session.execute(
            self.client_table.select().where(self.client_table.c.email == client_data["email"])
        ).fetchone()

        if existing_client:
            raise ValueError(f"Le champ 'email' est déjà utilisé par un autre client.")

        # Создаем объект клиента
        client = Client(**client_data)  # Передаем только необходимые поля

        # Валидация данных
        client.validate()

        # Подготовка данных для вставки
        new_client = {
            "full_name": client.full_name,
            "email": client.email,
            "phone": client.phone,
            "company_name": client.company_name,
            "creation_date": client.creation_date,
            "last_updated": client.last_updated,
            "commercial_contact": client.commercial_contact,
        }

        self.session.execute(self.client_table.insert().values(new_client))
        self.session.commit()

        return new_client
        
    def get_all_clients(self):
        result = self.session.execute(select(self.client_table)).fetchall()
        return [dict(row._mapping) for row in result]

    def search_clients(self, search_criteria):
        """Searches for clients based on various criteria."""
        print("Client search method called.")
        print(f"Search criteria: {search_criteria}")

        with Session(engine) as session:
            query = clients.select()

            # Check for full name search criteria
            if "full_name" in search_criteria and search_criteria["full_name"]:
                full_name_search = f"%{search_criteria['full_name'].strip()}%"
                query = query.where(clients.c.full_name.ilike(full_name_search))
                print(f"Searching by full name: {full_name_search}")

            # Check for email search criteria
            if "email" in search_criteria and search_criteria["email"]:
                email_search = f"%{search_criteria['email'].strip()}%"
                query = query.where(clients.c.email.ilike(email_search))
                print(f"Searching by email: {email_search}")

            # Check for company name search criteria
            if "company_name" in search_criteria and search_criteria["company_name"]:
                company_name_search = f"%{search_criteria['company_name'].strip()}%"
                query = query.where(clients.c.company_name.ilike(company_name_search))
                print(f"Searching by company name: {company_name_search}")

            result = session.execute(query).all()

            if not result:
                print("Erreur : Aucun client correspondant trouvé.")  # Error: No matching clients found.
            else:
                print(f"Clients trouvés : {len(result)}")  # Clients found: {len(result)}

            # Convert rows to dicts using _mapping
            return [dict(row._mapping) for row in result]

    def get_client_by_id(self, client_id):
        result = self.session.execute(select(self.client_table).where(self.client_table.c.id == client_id)).fetchone()
        if result:
            return {
                'id': result[0],
                'full_name': result[1],
                'email': result[2],
                'phone': result[3],
                'company_name': result[4],
                'creation_date': result[5],
                'last_updated': result[6],
                'commercial_contact': result[7]
            }
        return None

    def update_client(self, client_id, updated_data):
        try:
            current_client = self.get_client_by_id(client_id)

            if not current_client:
                return False  # Если клиент не найден, возвращаем False

            update_values = {}

            # Логика обновления значений
            if updated_data['full_name']:
                update_values['full_name'] = updated_data['full_name']
            else:
                update_values['full_name'] = current_client['full_name']

            if updated_data['email']:
                update_values['email'] = updated_data['email']
            else:
                update_values['email'] = current_client['email']

            if updated_data['phone']:
                update_values['phone'] = updated_data['phone']
            else:
                update_values['phone'] = current_client['phone']

            if updated_data['company_name']:
                update_values['company_name'] = updated_data['company_name']
            else:
                update_values['company_name'] = current_client['company_name']

            if updated_data['commercial_contact']:
                update_values['commercial_contact'] = updated_data['commercial_contact']
            else:
                update_values['commercial_contact'] = current_client['commercial_contact']

            update_values['last_updated'] = datetime.now()

            # Выполнение обновления в базе данных
            self.session.execute(
                clients.update().where(clients.c.id == client_id).values(update_values)
            )
            self.session.commit()
            return True  # Возвращаем True, если обновление прошло успешно
        except Exception as e:
            print(f"Error: {e}")
            return False  # Возвращаем False в случае ошибки