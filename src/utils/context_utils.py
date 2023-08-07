from hashlib import sha256


def hash_document(customer: str, document: str):
    input_string = f'{customer}-{document}'

    hash_object = sha256(input_string.encode())
    hex_dig = hash_object.hexdigest()
    return hex_dig
