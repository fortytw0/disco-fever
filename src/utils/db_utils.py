import sqlite3

from src.utils.config import *

class DB(object) : 

    def __init__(self, db_path:str) -> None:
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

        self.command_template = "select * from {} where {{}}".format(TABLE_NAME)


    def get(self, q:dict) -> list : 

        query = ""

        for key, item in q.items() : 
            query += "{}='{}' ".format(key, item)

        self.cursor.execute(self.command_template.format(query))
        return self.cursor.fetchall()

    def close_connection(self) -> None : 
        self.connection.close()

    

