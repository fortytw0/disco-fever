import os
import sqlite3

class DefaultRetrievedObject(object) : 
    pass


class DefaultRetriever(object) :

    def __init__(self, db_path:str, mode:str, model_name:str=None, table_name:str='wiki', entity_column:str='id', **kwargs) -> None:


        self.db_path = db_path
        self.mode = mode
        self.model_name = model_name
        self.model_dir = 'models/retriever/'
        self.model_path = os.path.join(self.model_dir, self.model_name)
        self.table_name = table_name
        self.entity_column = entity_column

        self.__sanity_check__()

        self.db_connection = sqlite3.connect(self.db_path)
        self.cursor = self.db_connection.cursor()
        self.fetch_command = "select * from {} {{}}".format(table_name)

    def get_cursor(self) -> sqlite3.Cursor : 
        return self.cursor

    def fetch_entity(self, entity:str) -> list :
        
        command = "where {}={}".format(self.entity_column, entity)
        self.fetch_command.format(command)
        self.cursor.execute()
        return self.cursor.fetchall()




    def __sanity_check__(self, **kwargs) : 
        pass




