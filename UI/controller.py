import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None



    # POPOLA DROPDOWN
    # TODO
    def popola_dropdown(self):
        """Popola i menu a tendina (Dropdown) con i dati provenienti dal Modello."""

        # 1. Popoliamo le biblioteche (mantenendo "Nessun filtro" e aggiungendo le nuove)
        biblioteche = self._model.get_biblioteche()
        opzioni_biblio = [ft.dropdown.Option("Nessun filtro")]
        for b in biblioteche:
            opzioni_biblio.append(ft.dropdown.Option(b.nome))
        self._view.dd_biblioteca.options = opzioni_biblio

        # 2. Popoliamo i generi (mantenendo "Nessun filtro" e aggiungendo i nuovi)
        generi = self._model.get_generi()
        opzioni_genere = [ft.dropdown.Option("Nessun filtro")]
        for genere in generi:
            opzioni_genere.append(ft.dropdown.Option(genere))
        self._view.dd_genere.options = opzioni_genere

        # Aggiorniamo la pagina per rendere visibili le opzioni
        self._view.page.update()

    # CALLBACKS DROPDOWN
    # TODO
    def seleziona_biblioteca(self, e):
        """Gestisce la scelta dell'utente nel dropdown delle biblioteche."""
        valore = e.control.value  # 🟢 Leggiamo direttamente dall'evento del controllo
        print(f"DEBUG -> Biblioteca selezionata: '{valore}'")

        if valore == "Nessun filtro" or not valore:
            self.biblioteca_selezionata = None
        else:
            self.biblioteca_selezionata = valore

    def seleziona_genere(self, e):
        """Gestisce la scelta dell'utente nel dropdown dei generi."""
        valore = e.control.value  # 🟢 Leggiamo direttamente dall'evento del controllo
        print(f"DEBUG -> Genere selezionato: '{valore}'")

        if valore == "Nessun filtro" or not valore:
            self.genere_selezionato = None
        else:
            self.genere_selezionato = valore

    # AZIONE: MOSTRA LIBRI
    # TODO
    def mostra_libri(self, e):

        # 🔍 STAMPIAMO I FILTRI ATTUALI NELLA CONSOLE DI PYCHARM
        print(f"DEBUG FILTRI -> Biblioteca: '{self.biblioteca_selezionata}' | Genere: '{self.genere_selezionato}'")

        """Legge i libri filtrati dal modello e aggiorna la ListView nella UI."""
        # Puliamo la lista attuale dei libri visibili
        self._view.list_view_libri.controls.clear()

        # Richiamiamo il modello passando i filtri correnti (None se non attivi)
        libri = self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)

        print(f"DEBUG RISULTATI -> Trovati {len(libri)} libri.")

        if not libri:
            # Se nessun libro soddisfa i criteri, mostriamo un alert
            self._view.show_alert("Nessun libro trovato con i criteri di filtraggio selezionati.")
        else:
            # Aggiungiamo ogni libro alla ListView della vista
            for libro in libri:
                testo_libro = f" {libro.titolo} — {libro.autore} ({libro.anno_pubblicazione}) | Genere: {libro.genere} "
                self._view.list_view_libri.controls.append(ft.Text(testo_libro))

        self._view.update()
