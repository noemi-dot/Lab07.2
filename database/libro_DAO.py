from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    # TODO
    def get_generi(self):
        """
        Recupera l'elenco di tutti i generi distinti dei libri presenti nel database.
        """
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            return result
        # Aggiunto buffered=True per evitare risultati non letti nel buffer
        cursor = cnx.cursor(dictionary=True,buffered=True)
        query = """SELECT DISTINCT genere FROM libro WHERE genere IS NOT NULL AND genere != '' ORDER BY genere"""

        try:
            cursor.execute(query)
            for row in cursor:
                result.append(row["genere"])
        except Exception as e:
            print(f"Errore durante il recupero dei generi: {e}")
        finally:
            cursor.close()
            cnx.close()

            return result


    def get_libri_filtrati(self, biblioteca_nome: str, genere: str):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            return result

        cursor = cnx.cursor(dictionary=True, buffered=True)

        # Aggiungiamo l.id_biblioteca alla SELECT
        query = """
               SELECT l.id, l.titolo, l.autore, l.genere, l.anno_pubblicazione, l.id_biblioteca, b.nome AS biblioteca_nome
               FROM libro l
               JOIN biblioteca b ON l.id_biblioteca = b.id
               WHERE 1=1
           """
        params = []

        if biblioteca_nome is not None:
            query += " AND b.nome = %s"
            params.append(biblioteca_nome)

        if genere is not None:
            query += " AND l.genere = %s"
            params.append(genere)

        try:
            cursor.execute(query, tuple(params))
            for row in cursor:
                # Passiamo tutti i parametri richiesti dal costruttore del DTO Libro
                libro = Libro(
                    id=row["id"],
                    titolo=row["titolo"],
                    autore=row["autore"],
                    genere=row["genere"],
                    anno_pubblicazione=row["anno_pubblicazione"],
                    id_biblioteca=row["id_biblioteca"]
                )
                result.append(libro)
        except Exception as e:
            print(f"Errore durante il filtraggio dei libri: {e}")
        finally:
            cursor.close()
            cnx.close()

        return result
