from hashlib import sha256


def hash_document_chunk(customer: str, document: str, chunk_index: int):
    input_string = f'{customer}-{document}-{chunk_index}'

    hash_object = sha256(input_string.encode())
    hex_dig = hash_object.hexdigest()
    return hex_dig
