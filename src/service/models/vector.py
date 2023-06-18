from dataclasses import dataclass


@dataclass
class DatabaseVector:
    embedder: object
    vector: list[int]
    metadata: dict
