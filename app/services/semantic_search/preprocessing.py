import nltk
from nltk import sent_tokenize

nltk.download("stopwords")
nltk.download("punkt")


def split_text(text: str, chunk_size: int, sentence_overlap: int):
    sentences = sent_tokenize(text)
    chunks = []
    i = 0

    while i < len(sentences):
        end_index = min(i + chunk_size, len(sentences))
        chunk = sentences[i:end_index]
        chunks.append(' '.join(chunk))
        i = i + (chunk_size - sentence_overlap)
    return chunks
