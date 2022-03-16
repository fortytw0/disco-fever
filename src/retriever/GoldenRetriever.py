import spacy
import json

from src.retriever.Retriever import DefaultRetrievedObject, DefaultRetriever

class GoldenRetriever(DefaultRetriever) : 

    def __init__(self, db_path: str, **kwargs) -> None:
        
        super().__init__(db_path, **kwargs)
        self.nlp = spacy.load('en_core_web_sm')
        

    def _extract_entities(self, claim:str) -> list : 
        return self.nlp(claim).ents

    def _fetch_entity(self, entity_name:str) -> list :
        return self.db.get({self.entity_column:entity_name})

    def retrieve(self, claim: str) -> DefaultRetrievedObject:
        entities = [entity.text for entity in self._extract_entities(claim)]
        retrieved = DefaultRetrievedObject()

        for entity in entities : 
            entity_document = self._fetch_entity(entity)
            retrieved.add(json.loads(entity_document))


        return retrieved

