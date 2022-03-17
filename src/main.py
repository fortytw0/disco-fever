from src.retriever.GoldenRetriever import GoldenRetriever
from src.encoder.Zencoder import Zencoder


golden_retriever = GoldenRetriever(db_path='data/feverous_wikiv1.db', mode='train', model_name='default')
zencoder = Zencoder()

claim = 'J. K. Rowling wrote Harry Potter'
fetched_entites = golden_retriever.retrieve(claim)
zencoder.encode(claim, fetched_entites)

print(fetched_entites)
print(type(fetched_entites))
