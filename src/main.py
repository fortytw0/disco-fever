from src.retriever.GoldenRetriever import GoldenRetriever


golden_retriever = GoldenRetriever(db_path='data/feverous_wikiv1.db', mode='train', model_name='default')
fetched_entites = golden_retriever.retrieve('J. K. Rowling wrote Harry Potter')

print(fetched_entites)
print(type(fetched_entites))