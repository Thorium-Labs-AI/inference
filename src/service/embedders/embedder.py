class Embedder:

    def __init__(self, model: str):
        self.model = model

    def get_embedding(self, embedding_input: str, user_id: str):
        raise NotImplementedError("Please use a subclass.")
