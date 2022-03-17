from typing import Tuple
import spacy
import json

from src.retriever.Retriever import DefaultRetrievedObject, DefaultRetriever
from src.utils.config import RETRIEVED_DOCUMENT_ORDER_COLUMN, RETRIEVED_DOCUMENT_TITLE_COLUMN


class GoldenRO(DefaultRetrievedObject) : 

    def __init__(self, contents: list = []) -> None:
        super().__init__(contents)

    def extract(self) -> tuple:
        
        sentences = []
        info = []
        for document in self.contents : 
            for sentence_order  in document[RETRIEVED_DOCUMENT_ORDER_COLUMN] : 
                sentences.append(document[sentence_order])
                info.append((document[RETRIEVED_DOCUMENT_TITLE_COLUMN], sentence_order))

        return (sentences, info)


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
        retrieved = GoldenRO()

        for entity in entities : 
            entity_documents = self._fetch_entity(entity)
            for entity_document in entity_documents : 

                retrieved.add(json.loads(entity_document[1]))


        return retrieved

