from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich import box

class EventView:
    console = Console()
    
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
        print("1. Voir tous les événements assignés")
        print("2. Voir mes événements")
        print("3. Mettre à jour les informations de mes événements")
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


    def get_event_id():
        """Get event ID from user input."""
        while True:
            event_id = input("Entrez l'ID de l'événement : ").strip()
            if not event_id:  
                print("L'ID de l'événement ne peut pas être vide. Veuillez entrer une valeur valide.")
                continue  
            return event_id

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
            name = input("Nom de l'événement : ").strip()
            start_date = cls.parse_date(input("Date de début (DD/MM/YYYY HH:MM) : "))
            end_date = cls.parse_date(input("Date de fin (DD/MM/YYYY HH:MM) : "))
            location = input("Lieu : ").strip()
            num_attendees = int(input("Nombre de participants : "))
            notes = input("Notes (optionnel) : ")
            
            if not name or not start_date or not end_date or not location or not num_attendees:
                raise ValueError("Tous les champs sauf 'Notes' sont obligatoire et ne peuvent pas être vides.")

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
    def get_updated_event_data(cls):
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
        """Display a list of events using Rich table."""
        EventView.console.print("\n[bold cyan]Liste des événements:[/bold cyan]\n")

        if not events:
            EventView.console.print("[bold red]Aucun événement trouvé.[/bold red]")
            return
        
        table = Table(show_header=True, header_style="bold cyan", box=box.SQUARE)
        table.add_column("ID", style="dim", width=6)
        table.add_column("Nom de l'événement", style="bold blue")
        table.add_column("Date de début", style="white")
        table.add_column("Date de fin", style="white")
        table.add_column("Lieu", style="green")
        table.add_column("Participants", style="white")
        table.add_column("Client", style="white")
        table.add_column("Client contact", style="white")
        table.add_column("Support", style="yellow")
        table.add_column("Notes", style="white")

        for event in events:
            support_contact_name = event.support_contact.username if event.support_contact else "Non assigné"
            table.add_row(
                str(event.id),
                event.name,
                event.start_date.strftime('%d/%m/%Y %H:%M'),
                event.end_date.strftime('%d/%m/%Y %H:%M'),
                event.location,
                str(event.num_attendees),
                event.client.company_name,
                event.client.phone,
                support_contact_name,
                event.notes
            )

        EventView.console.print(table)

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
            event_id = int(input("\nEntrez l'ID de l'événement : "))

            support_id_input = input("Entrez l'ID du contact support : ")
            support_id = int(support_id_input) if support_id_input else None

            return event_id, support_id

        except ValueError:
            print("Erreur : ID invalide. Veuillez entrer un nombre.")
            return None, None

    @staticmethod
    def display_event_details(event):
        """Affiche les détails d'un événement."""
        print("\n Détail d'un événements :\n")
        support_contact_name = event.support_contact.username if event.support_contact else "Non assigné"
        print(f"Nome de l'événement: {event.name}")
        print(f"Date de début: {event.start_date.strftime('%d/%m/%Y %H:%M')}")
        print(f"Date de fin: {event.end_date.strftime('%d/%m/%Y %H:%M')}")
        print(f"Lieu: {event.location}")
        print(f"Nombre de participants: {event.num_attendees}")
        print(f"Client: {event.client.company_name}")
        print(f"Support: {support_contact_name}")
        if event.notes:
            print(f"Notes: {event.notes}")
