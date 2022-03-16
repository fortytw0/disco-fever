import spacy

from src.retriever.Retriever import DefaultRetrievedObject, DefaultRetriever

class GoldenRetriever(DefaultRetriever) : 

    def __init__(self, db_path: str, mode: str, model_name: str = None, **kwargs) -> None:
        
        super().__init__(db_path, mode, model_name, **kwargs)
        self.nlp = spacy.load('en_core_web_sm')
        

    def _extract_entities(self, claim:str) -> list : 
        return self.nlp(claim).ents

    def _fetch_entity(self, entity_name:str) -> list :
        return self.db.get({self.entity_column:entity_name})

    def retrieve(self, claim: str) -> DefaultRetrievedObject:
        entities = [entity.text for entity in self._extract_entities(claim)]
        retrieved = DefaultRetrievedObject()

        for entity in entities : 
            retrieved.add(self.db.get(entity))

        return retrieved

