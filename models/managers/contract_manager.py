from datetime import datetime

from sqlalchemy.orm import sessionmaker

from config import engine
from models import Contract


class ContractManager:
    def __init__(self):
        self.Session = sessionmaker(bind=engine)

    def add_contract(self, contract_data, session):
        """Create a new contract."""
        contract = Contract(**contract_data)
        session.add(contract)
        session.commit()
        return contract
    
    def get_all_contracts(self):
        with self.Session() as session:
            return session.query(Contract).all()

    def search_contracts(self, search_criteria):
        with self.Session() as session:
            query = session.query(Contract)
            if "client_id" in search_criteria:
                query = query.filter(Contract.client_id.ilike(f"%{search_criteria['client_id']}%"))
            if "client" in search_criteria:
                query = query.filter(Contract.client.ilike(f"%{search_criteria['client']}%"))

    def get_contract_by_id(self, contract_id):
        with self.Session() as session:
            return session.query(Contract).get(contract_id)

    def update_contract(self, contract_id, updated_data):
        with self.Session() as session:
            contract = session.query(Contract).get(contract_id)
            if not contract:
                return False

            for key, value in updated_data.items():
                if value is not None:
                    setattr(contract, key, value)

            contract.last_updated = datetime.now()
            session.commit()
            return contract
