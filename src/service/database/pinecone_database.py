from src.service.models.vector import DatabaseVector


class Database:
    def __init__(self):
        pass

    def define_index(self, index_name: str, index_dims: int, metric: str):
        if index_name.find(".") != -1:
            raise ValueError("Index name cannot contain '.'")

        prefix = "client"
        suffix = "vectors"
        self.create_index(f'{prefix}.{index_name}.{suffix}', index_dims, metric)

    def create_index(self, qualified_index_name: str, index_dims: int, metric: str):
        raise NotImplementedError
        pass

    def delete_index(self, index_name: str):
        raise NotImplementedError
        pass

    def get_index(self, index_name: str):
        raise NotImplementedError
        pass

    def insert_vectors(self,  vectors: list[DatabaseVector], index_name: str):
        raise NotImplementedError
        pass
