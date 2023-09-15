import nltk
from nltk import sent_tokenize

nltk.download("stopwords")
nltk.download("punkt")


def remove_stopwords(text: str) -> str:
    stopwords = nltk.corpus.stopwords.words('english')
    raw_tokens = text.split(' ')
    processed_tokens = ' '.join([i for i in raw_tokens if i not in stopwords])
    return processed_tokens


def create_chunk_contents(text: str, chunk_size: int, sentence_overlap: int):
    sentences = sent_tokenize(text)
    chunks = []
    i = 0

    while i < len(sentences):
        end_index = min(i + chunk_size, len(sentences))
        chunk = sentences[i:end_index]
        chunks.append(' '.join(chunk))
        i = i + (chunk_size - sentence_overlap)
    return chunks
