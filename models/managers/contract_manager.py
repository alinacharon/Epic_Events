from datetime import datetime

from sqlalchemy.orm import sessionmaker, joinedload

from config import engine
from models import Contract
from sentry_logging import log_crud_operation


class ContractManager:
    def __init__(self):
        self.Session = sessionmaker(bind=engine)
        
    @log_crud_operation("create")
    def add_contract(self, contract_data):
        """Create a new contract."""
        with self.Session() as session:
            contract = Contract(**contract_data)
            session.add(contract)
            session.commit()
            session.refresh(contract)
            return contract

    def get_all_contracts(self):
        """Retrieve all contracts with related data (e.g., commercial)."""
        with self.Session() as session:
            return session.query(Contract).options(joinedload(Contract.commercial)).all()

    def get_contract_by_id(self, contract_id):
        """Retrieve a contract by ID with related commercial and client data."""
        with self.Session() as session:
            return session.query(Contract).options(
                joinedload(Contract.commercial),
                joinedload(Contract.client)
            ).get(contract_id)

    def get_contracts_by_commercial(self, commercial_id):
        """Retrieve contracts for a specific commercial with related data."""
        with self.Session() as session:
            contracts = session.query(Contract).options(joinedload(Contract.commercial)) \
                .filter(Contract.commercial_id == commercial_id).all()
            return contracts
        
    @log_crud_operation("update")
    def update_contract(self, contract_id, updated_data):
        """Update a contract using provided data and commit changes."""
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
        """Retrieve all unsigned contracts."""
        with self.Session() as session:
            return session.query(Contract).filter(Contract.signed == False).all()

    def get_not_fully_paid_contracts(self):
        """Retrieve contracts that are not fully paid."""
        with self.Session() as session:
            return session.query(Contract).filter(Contract.remaining_amount > 0).all()
