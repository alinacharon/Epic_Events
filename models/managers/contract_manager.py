from datetime import datetime

from sqlalchemy.orm import sessionmaker

from config import engine
from models import Contract, Client


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
        """Search for contracts based on the given criteria."""
        with self.Session() as session:
            query = session.query(Contract)

            if "client_id" in search_criteria:
                query = query.filter(Contract.client_id.ilike(
                    f"%{search_criteria['client_id']}%"))

            if "client" in search_criteria:
                query = query.join(Client).filter(
                    Client.full_name.ilike(f"%{search_criteria['client']}%"))

            return query.all()

    def get_contract_by_id(self, contract_id, session):
        with self.Session() as session:
            return session.query(Contract).get(contract_id)

    def get_contracts_by_commercial(self, commercial_id):
        with self.Session() as session:
            contracts = session.query(Contract).filter(
                Contract.commercial_id == commercial_id).all()
            return contracts

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

    def get_unsigned_contracts(self):
        """Получить все неподписанные контракты."""
        with self.Session() as session:
            return session.query(Contract).filter(Contract.signed == False).all()

    def get_not_fully_paid_contracts(self):
        """Получить все контракты, которые не полностью оплачены."""
        with self.Session() as session:
            return session.query(Contract).filter(Contract.remaining_amount > 0).all()