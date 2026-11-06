from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    # TODO
    def get_biblioteche(self):
        """
        Recupera tutte le biblioteche presenti nel database.
        Restituisce una lista di oggetti Biblioteca (DTO).
        """
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Errore di connessione al database.")
            return result
        # Aggiunto buffered=True per evitare risultati non letti nel buffer
        cursor = cnx.cursor(dictionary=True, buffered=True)
        # Query per selezionare tutte le biblioteche ordinate per nome o ID
        query = """SELECT id, nome, indirizzo FROM biblioteca"""

        try:
            cursor.execute(query)
            for row in cursor:
                # Creazione dell'oggetto DTO Biblioteca
                biblioteca = Biblioteca(id=row["id"], nome=row["nome"], indirizzo=row["indirizzo"])
                result.append(biblioteca)
        except Exception as e:
            print(f"Errore durante la query delle biblioteche: {e}")
        finally:
            cursor.close()
            cnx.close()

        return result