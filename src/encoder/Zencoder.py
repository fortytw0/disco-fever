from src.retriever.Retriever import DefaultRetrievedObject
from src.encoder.Encoder import DefaultEncoder, DefaultEncodedObject
from transformers import TFBertModel, BertTokenizer

import numpy as np
from scipy.spatial import distance

class Zencoder(DefaultEncoder) :

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        self.bert = TFBertModel.from_pretrained('bert-base-uncased')
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

    
    def _get_bert_repr(self, sentences:list) : 
        
        repr = []

        for sentence in sentences : 
            tokenized = self.tokenizer(sentences, return_tensors='tf', padding=True)
            output = self.bert(tokenized)
            repr.append(output.last_hidden_state[:, 0, : ].numpy())

        return repr

    def _calculate_cosine_similarity(self, claim_repr:np.array, sentences_repr:np.array) -> np.array : 

        cosine_similarities = [distance.cosine(claim_repr, sentence_repr) for sentence_repr in sentences_repr]
        return np.array(cosine_similarities)


    def encode(self, claim:str, retrieved:DefaultRetrievedObject, top_k:int=10) : 

        sentences, info = retrieved.extract()
        claim_repr = self._get_bert_repr([claim])[0]

        print('claim_repr.shape : ' , claim_repr.shape)

        sentences_repr = self._get_bert_repr(sentences)

        print('sentences_repr.shape : ', sentences_repr.shape)

        cosine_similarities = self._calculate_cosine_similarity(claim_repr, sentences_repr)

        most_similar_indices = np.argsort(cosine_similarities)

        for i in most_similar_indices : 

            print('\n')
            print(sentences[i])
            print(info[i])
            print(cosine_similarities[i])




    

    