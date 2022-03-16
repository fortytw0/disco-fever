import os
import sqlite3
import spacy

from src.utils.db_utils import DB
from src.utils.config import ID_COLUMN_NAME, RETRIEVED_DOCUMENT_TITLE_NAME

class DefaultRetrievedObject(object) : 
    
    def __init__(self, contents:list=[]) -> None:
        
        self.contents = contents
        self.entity_column = RETRIEVED_DOCUMENT_TITLE_NAME

    def __str__(self) : 
        return '\t'.join([content[self.entity_column] for content in self.contents])

    def add(self, document:dict) -> None : 
        self.contents.append(document)

    def process(self) -> None : 
        pass


class DefaultRetriever(object) :

    def __init__(self, db_path:str, **kwargs) -> None:


        self.db = DB(db_path)
        self.entity_column = ID_COLUMN_NAME

        self.__sanity_check__()

    
    def _extract_entities(self, claim:str) -> list : 
        pass  


    def _fetch_entity(self, entity_name:str) -> list :
        pass

    def retrieve(self, claim:str) -> DefaultRetrievedObject : 
        pass

    def __sanity_check__(self, **kwargs) : 
        pass




