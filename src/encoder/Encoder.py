from src.retriever.Retriever import DefaultRetrievedObject

class DefaultEncodedObject(object): 

    def __init__(self) : 
        pass


class DefaultEncoder(object)  :

    def __init__(self, **kwargs) -> None :
        pass

    def encode(self, retrieved:DefaultRetrievedObject) -> DefaultEncodedObject :
        pass
