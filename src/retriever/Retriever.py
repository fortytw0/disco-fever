import os
import sqlite3
import spacy

from src.utils.db_utils import DB

class DefaultRetrievedObject(object) : 
    
    def __init__(self, contents:list=[]) -> None:
        
        self.contents = contents
        self.entity_column = 'id'

    def __str__(self) : 

        for content in self.contents : 
            print(content[self.entity_column])

    def add(self, document:dict) -> None : 
        self.contents.append(document)

    def process(self) -> None : 
        pass


class DefaultRetriever(object) :

    def __init__(self, db_path:str, **kwargs) -> None:


        self.db = DB(db_path)
        self.entity_column = 'id'

        self.__sanity_check__()

    
    def _extract_entities(self, claim:str) -> list : 
        pass  


    def _fetch_entity(self, entity_name:str) -> list :
        pass

    def retrieve(self, claim:str) -> DefaultRetrievedObject : 
        entities = self._extract_entities(claim)
        retrieved_collection = DefaultRetrievedObject()

        for entity in entities : 
            retrieved_document = self._fetch_entity(entity)
            retrieved_collection.add(retrieved_document)

        return retrieved_collection


    def __sanity_check__(self, **kwargs) : 
        pass




