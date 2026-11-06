import flet as ft
from UI.alert import AlertManager

'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """
        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Biblioteche di Torino", size=38, weight=ft.FontWeight.BOLD)

        # --- Sezione 2: Filtraggio ---
        # TODO
        # Dropdown per selezionare la biblioteca
        self.dd_biblioteca = ft.Dropdown(
            label="Biblioteca",
            hint_text="Seleziona una biblioteca",
            width=300,
            options=[ft.dropdown.Option("Nessun filtro")],  # <-- Le opzioni partono già qui
            on_select=lambda e: self.controller.seleziona_biblioteca(e)
        )

        # Dropdown per selezionare il genere
        self.dd_genere = ft.Dropdown(
            label="Genere",
            hint_text="Seleziona un genere",
            width=300,
            options=[ft.dropdown.Option("Nessun filtro")],  # <-- Le opzioni partono già qui
            on_select=lambda e: self.controller.seleziona_genere(e)
        )
        # --- Sezione 3: Libri ---
        # Pulsante per avviare la ricerca con i filtri
        self.btn_mostra_libri = ft.Button(
            content="Mostra Libri",    #scrivo "content" invece di "text" (per la nuova versione di Flet)
            width=200,
            on_click=lambda e: self.controller.mostra_libri(e)
        )

        # ListView per mostrare i risultati in modo scorrevole
        self.list_view_libri = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=False)

        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            ft.Divider(),

            # Sezione 2: Filtraggio
            ft.Row(
                controls=[self.dd_biblioteca, self.dd_genere],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Divider(),

        # Sezione 3: Libri
        # TODO
            ft.Row(
                controls=[self.btn_mostra_libri],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Container(
                content=self.list_view_libri,
                height=350,
                border_radius=10,
                padding=10,
            )
        )

        self.page.scroll = "adaptive"

        # 🟢 ORA I COMPONENTI ESISTONO: possiamo popolare i dropdown in sicurezza!
        if self.controller:
            self.controller.popola_dropdown()


        self.page.update()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()
