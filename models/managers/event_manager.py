from sqlalchemy.orm import sessionmaker, joinedload

from config import engine
from models import Event, User, Client


class EventManager:
    def __init__(self):
        self.Session = sessionmaker(bind=engine)

    def add_event(self, event_data):
        """Add a new event."""
        with self.Session() as session:
            event = Event(**event_data)
            session.add(event)
            session.commit()
            session.refresh(event)
            return event

    def get_all_events(self):
        """Retrieve all events with joined commercial and support details."""
        with self.Session() as session:
            events = session.query(Event).options(
                joinedload(Event.client),
                joinedload(Event.support_contact)
            ).all()
            return events

    def get_event_by_id(self, event_id):
        """Retrieve event details by ID with related data."""
        with self.Session() as session:
            event = session.query(Event).options(joinedload(
                Event.client), joinedload(Event.support_contact)).get(event_id)
            return event

    def get_events_by_client(self, client_id):
        """Retrieve events for a specific client."""
        with self.Session() as session:
            events = session.query(Event).options(joinedload(Event.client), joinedload(Event.support_contact)) \
                .filter(Event.client_id == client_id).all()
            return events

    def update_event(self, event_id, updated_data):
        """Update event information."""
        with self.Session() as session:
            event = session.query(Event).options(joinedload(Event.client), joinedload(Event.support_contact)).get(
                event_id)
            if not event:
                return None

            # Update fields
            for key, value in updated_data.items():
                if value is not None:
                    setattr(event, key, value)

            session.commit()
            return event

    def assign_support_to_event(self, event_id, support_id):
        """Assign a support contact to an event."""
        with self.Session() as session:
            event = session.query(Event).get(event_id)
            if not event:
                return None

            support_user = session.query(User).filter_by(id=support_id).first()
            if not support_user:
                return None

            event.support_contact = support_user
            session.commit()
            session.refresh(event)
            return event

    def get_unassigned_events(self):
        """Get all events without an assigned support contact, with joined loading of related data."""
        with self.Session() as session:
            return session.query(Event).options(
                joinedload(Event.client),
                joinedload(Event.support_contact)
            ).filter(
                Event.support_contact_id == None
            ).all()

    def get_assigned_events(self):
        """Get all events with an assigned support contact, with joined loading of related data."""
        with self.Session() as session:
            return session.query(Event).options(
                joinedload(Event.client),
                joinedload(Event.support_contact)
            ).filter(
                Event.support_contact_id != None
            ).all()

    def get_events_by_support(self, support_contact_id: int):
        """Get events with a specific assigned support contact."""
        with self.Session() as session:
            events = (
                session.query(Event)
                .options(joinedload(Event.client), joinedload(Event.contract), joinedload(Event.support_contact))
                .filter(Event.support_contact_id == support_contact_id)
                .all()
            )
            return events

    def get_events_by_commercial(self, commercial_id: int):
        """Get events with a specific commercial."""
        with self.Session() as session:
            events = (
                session.query(Event)
                .join(Event.client)
                .filter(Client.commercial_id == commercial_id)
                .options(joinedload(Event.client), joinedload(Event.contract), joinedload(Event.support_contact))
                .all()
            )
            return events
