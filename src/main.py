from src.retriever.Retriever import DefaultRetriever


default_retriever = DefaultRetriever(db_path='data/feverous_wikiv1.db', mode='train', model_name='default')
fetched_entites = default_retriever.fetch_entity()

print(fetched_entites)
print(type(fetched_entites))