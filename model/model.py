from database.biblioteca_DAO import BibliotecaDAO
from database.libro_DAO import LibroDAO

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di BibliotecaDAO e LibroDAO)
'''

class Model:
    def __init__(self):
        self._biblioteca_dao = BibliotecaDAO()
        self._libro_dao = LibroDAO()

#ADESSO RICHIAMO SEMPLICEMENTE LE FUNZIONI CHE HO FATTO NEL DAO. (tutto fatto grazie alle query)

    # --- LIBRI ---
    def get_libri_filtrati(self, biblioteca:str, genere:str):
        """Restituisce la lista di tutti i libri filtrati per biblioteca e/o genere (filtri opzionali)."""
        # TODO
        return self._libro_dao.get_libri_filtrati(biblioteca, genere)

    def get_generi(self):
        """Restituisce la lista di tutti i generi."""
        # TODO
        return self._libro_dao.get_generi()

    # --- BIBLIOTECHE ---
    def get_biblioteche(self):
        """ Restituisce la lista di tutte le biblioteche."""
        # TODO
        return self._biblioteca_dao.get_biblioteche()

