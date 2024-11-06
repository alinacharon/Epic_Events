from models import EventManager
from views.event_view import EventView
from views.main_view import MainView

# 3. Gestion des événements
#    - Créer un événement
#    - Consulter la liste des événements
#    - Filtres des événements
#      * Événements sans support attribué
#      * Mes événements (selon le rôle)
#    - Modifier un événement

class EventtController:

    def __init__(self):
        database_url = "postgresql://admin:mypassword@localhost/database"
        self.event_manager = EventManager(database_url)

    def event_menu(self):
        # Main Event management menu loop
        while True:
            choice = EventView.manage_events_menu()
            match choice:
                case "1":
                    self.create_event()
                case "2":
                    self.list_all_events()
                case "3":
                    self.search_events()
                case "4":
                    self.update_events()
                case "b":
                    break
                case "q":
                    MainView.print_exit()
                    exit()
                case _:
                    MainView.print_invalid_input()
                    continue
                
    def event_sub_menu(self):
        # Sub Event management menu loop
        while True:
            choice = EventView.manage_events_menu()
            match choice:
                case "1":
                    self.get_unassigned_events()
                case "2":
                    self.get_my_events()
                case "b":
                    break
                case "q":
                    MainView.print_exit()
                    exit()
                case _:
                    MainView.print_invalid_input()
                    continue