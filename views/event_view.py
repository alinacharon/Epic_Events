from datetime import datetime
from typing import Dict, Optional


class EventView:
    # MANAGEMENT TEAM
    @classmethod
    def management_events_menu(cls):
        """Display the management event menu."""
        print("\nGestion des événements (Management):")
        print("1. Voir tous les événements")
        print("2. Filtrer les événements")
        print("3. Assigner un support")
        print("b. Retour")
        print("q. Quitter")
        return input("Choisissez une option : ").strip()

    # SUPPORT TEAM

    @classmethod
    def support_events_menu(cls):
        """Отображает меню для роли SUPPORT."""
        print("\nGestion des événements (Support) :")
        print("1. Voir les événements assignés")
        print("2. Mettre à jour les informations des événements assignés")
        print("3. Filtrer les événements (par exemple, uniquement ceux qui me sont assignés)")
        print("b. Retour")
        print("q. Quitter")
        return input("Choisissez une option : ").strip()
    
    #COMMERCIAL MENU 
    
    @classmethod
    def commercial_events_menu(cls):
        """Отображает меню для роли COMMERCIAL."""
        print("\nGestion des événements (Commerciale):")
        print("1. Créer un nouvel événement pour un client avec un contrat signé")
        print("2. Voir les événements")
        print("b. Retour")
        print("q. Quitter")
        return input("Choisissez une option : ").strip()

    @classmethod
    def event_search_menu(cls):
        """Display the event search menu."""
        print("\nRecherche d'événements:")
        print("1. Événements sans support attribué")
        print("2. Mes événements")
        print("b. Retour")
        print("q. Quitter")
        return input("Choisissez une option : ").strip()

    @staticmethod
    def get_event_id():
        """Get event ID from user input."""
        return input("Entrez l'ID de l'événement : ").strip()
    
    
    @staticmethod
    def parse_date(date_str: str) -> datetime:
        """Parse date string to datetime object."""
        try:
            return datetime.strptime(date_str, "%Y-%m-%d %H:%M")
        except ValueError:
            raise ValueError("Format de date invalide. Utilisez YYYY-MM-DD HH:MM")
    

    @classmethod
    def get_event_data(cls):
        """Collect event information from user input."""
        print("\nEntrez les informations de l'événement:")
        try:
            start_date = cls.parse_date(input("Date de début (YYYY-MM-DD HH:MM) : "))
            end_date = cls.parse_date(input("Date de fin (YYYY-MM-DD HH:MM) : "))
            location = input("Lieu : ")
            num_attendees = int(input("Nombre de participants : "))
            notes = input("Notes (optionnel) : ")
            support_contact_id = int(input("ID du contact support : "))

            return {
                "start_date": start_date,
                "end_date": end_date,
                "location": location,
                "num_attendees": num_attendees,
                "notes": notes if notes else None,
                "support_contact_id": support_contact_id
            }
        except ValueError as e:
            raise ValueError(f"Erreur de saisie : {str(e)}")

    @staticmethod
    def display_event_details(event: 'Event') -> None:
        """Display detailed information about an event."""
        print("\nInformations sur l'événement:")
        print(f"ID : {event.id}")
        print(f"Date de début : {event.start_date.strftime('%Y-%m-%d %H:%M')}")
        print(f"Date de fin : {event.end_date.strftime('%Y-%m-%d %H:%M')}")
        print(f"Lieu : {event.location}")
        print(f"Nombre de participants : {event.num_attendees}")
        print(f"Notes : {event.notes if event.notes else 'Aucune'}")
        print(f"ID du contrat : {event.contract_id}")
        print(f"ID du client : {event.client_id}")
        print(f"ID du contact support : {event.support_contact_id}")

    @classmethod
    def get_updated_event_data(cls) -> Dict[str, Optional[str]]:
        """Collect updated data for editing an event."""
        print("\nEntrez les informations mises à jour (laissez vide pour conserver la valeur actuelle):")
        updates = {}

        start_date = input("Date de début (YYYY-MM-DD HH:MM) : ")
        if start_date:
            updates["start_date"] = cls.parse_date(start_date)

        end_date = input("Date de fin (YYYY-MM-DD HH:MM) : ")
        if end_date:
            updates["end_date"] = cls.parse_date(end_date)

        location = input("Lieu : ")
        if location:
            updates["location"] = location

        num_attendees = input("Nombre de participants : ")
        if num_attendees:
            updates["num_attendees"] = int(num_attendees)

        notes = input("Notes : ")
        if notes:
            updates["notes"] = notes

        support_contact_id = input("ID du contact support : ")
        if support_contact_id:
            updates["support_contact_id"] = int(support_contact_id)

        return updates

    @staticmethod
    def display_event_list(events):
        """Display a list of events."""
        print("\nListe des événements:")
        if not events:
            print("Aucun événement trouvé.")
            return

        for event in events:
            print(
                f"- ID: {event.id}, "
                f"Date: {event.start_date.strftime('%Y-%m-%d %H:%M')}, "
                f"Lieu: {event.location}, "
                f"Participants: {event.num_attendees}, "
                f"Client: {event.client_id}, "
                f"Support: {event.support_contact_id}"
            )

    @classmethod
    def get_search_criteria(cls):
        """Get search criteria from user."""
        print("\nCritères de recherche (laissez vide pour ignorer):")
        criteria = {}

        location = input("Lieu : ")
        if location:
            criteria["location"] = location

        start_date = input("Date de début (YYYY-MM-DD HH:MM) : ")
        if start_date:
            criteria["start_date"] = cls.parse_date(start_date)

        end_date = input("Date de fin (YYYY-MM-DD HH:MM) : ")
        if end_date:
            criteria["end_date"] = cls.parse_date(end_date)

        client_id = input("ID du client : ")
        if client_id:
            criteria["client_id"] = int(client_id)

        support_contact_id = input("ID du contact support : ")
        if support_contact_id:
            criteria["support_contact_id"] = int(support_contact_id)

        return criteria

    @classmethod
    def filter_events_menu(cls):
        """Display the filter events menu and get user's choice."""
        print("\n--- Menu de Filtrage des Événements ---")
        print("1. Afficher les événements non assignés")
        print("2. Afficher les événements par date")
        print("3. Afficher les événements par client")
        print("b. Retour au menu précédent")

        choice = input("Choisissez une option : ")
        return choice
