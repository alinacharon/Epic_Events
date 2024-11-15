from datetime import datetime
from typing import Dict, Optional


class EventView:
    # MANAGEMENT TEAM
    @classmethod
    def management_events_menu(cls):
        """Display the event menu for MANAGEMENT."""
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
        """Display the event menu for SUPPORT."""
        print("\nGestion des événements (Support) :")
        print("1. Voir les événements assignés")
        print("2. Mettre à jour les informations des événements assignés")
        print("3. Voir mes événements")
        print("b. Retour")
        print("q. Quitter")
        return input("Choisissez une option : ").strip()

    # COMMERCIAL MENU

    @classmethod
    def commercial_events_menu(cls):
        """Display the event menu for COMMERCIAL."""
        print("\nGestion des événements (Commerciale):")
        print("1. Créer un nouvel événement pour un client avec un contrat signé")
        print("2. Voir tous les événements")
        print("3. Voir les événements de mes clients")
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
            return datetime.strptime(date_str, '%d/%m/%Y %H:%M')
        except ValueError:
            raise ValueError(
                "Format de date invalide. Utilisez DD/MM/YYYY HH:MM")

    @classmethod
    def get_event_data(cls):
        """Collect event information from user input."""
        print("\nEntrez les informations de l'événement:")
        try:
            name = input("Nom de l'événement : ") 
            start_date = cls.parse_date(input("Date de début (DD/MM/YYYY HH:MM) : "))
            end_date = cls.parse_date(input("Date de fin (DD/MM/YYYY HH:MM) : "))
            location = input("Lieu : ")
            num_attendees = int(input("Nombre de participants : "))
            notes = input("Notes (optionnel) : ")

            return {
                "name": name, 
                "start_date": start_date,
                "end_date": end_date,
                "location": location,
                "num_attendees": num_attendees,
                "notes": notes if notes else None,
            }
        except ValueError as e:
            raise ValueError(f"Erreur de saisie : {str(e)}")

    @classmethod
    def get_updated_event_data(cls) -> Dict[str, Optional[str]]:
        """Collect updated data for editing an event."""
        print("\nEntrez les informations mises à jour (laissez vide pour conserver la valeur actuelle):")
        updates = {}

        name = input("Nom de l'événement : ")
        if name:
            updates["name"] = name

        start_date = input("Date de début (DD/MM/YYYY HH:MM) : ")
        if start_date:
            updates["start_date"] = cls.parse_date(start_date)

        end_date = input("Date de fin (DD/MM/YYYY HH:MM) : ")
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
            support_contact_name = event.support_contact.username if event.support_contact else "Non assigné"
            print(
                f"- ID: {event.id}, "
                f"Nom: {event.name}, " 
                f"Date: {event.start_date.strftime('%d/%m/%Y %H:%M')}, "
                f"Lieu: {event.location}, "
                f"Participants: {event.num_attendees}, "
                f"Client: {event.client.company_name}, "
                f"Support: {support_contact_name}"
            )

    @classmethod
    def filter_events_menu(cls):
        """Display the filter events menu and get user's choice."""
        print("\n--- Menu de Filtrage des Événements ---")
        print("1. Afficher les événements non assignés")
        print("2. Afficher les événements par client")
        print("b. Retour au menu précédent")

        choice = input("Choisissez une option : ")
        return choice

    @staticmethod
    def get_support_assignment_data():
        """Prompt the user to enter the event ID and support contact ID for assignment."""
        try:
            # Ввод ID события
            event_id = int(input("Entrez l'ID de l'événement : "))
            
            # Ввод ID сотрудника службы поддержки
            support_id_input = input("Entrez l'ID du contact support (ou laissez vide pour aucun) : ")
            support_id = int(support_id_input) if support_id_input else None
            
            return event_id, support_id

        except ValueError:
            print("Erreur : ID invalide. Veuillez entrer un nombre.")
            return None, None