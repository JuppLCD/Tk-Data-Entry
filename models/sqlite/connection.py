import os
import sqlite3
import logging


class Connection:
    def __init__(self):
        # Construimos la ruta completa a la carpeta donde se guardara la DB
        ruta_actual = os.path.abspath(os.path.dirname(__file__))
        base_datos = os.path.join(ruta_actual, '..', '..', 'db', 'data.db')

        self.db = base_datos

    def _run_query(self, query, parameters=()):
        try:
            with sqlite3.connect(self.db) as conn:
                cursor = conn.cursor()
                result = cursor.execute(query, parameters)
                conn.commit()
                return result
        except Exception as e:
            logging.exception(e)
