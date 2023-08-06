import nltk
from nltk import sent_tokenize


def remove_stopwords(text: str) -> str:
    stopwords = nltk.corpus.stopwords.words('english')
    raw_tokens = text.split(' ')
    processed_tokens = ' '.join([i for i in raw_tokens if i not in stopwords])
    return processed_tokens


def create_chunks(text: str, token_overlap: int, max_chars: int = 0):
    # TODO: implement max_chars limit
    sentences = sent_tokenize(text)
    chunks = [sentences[i:i + 5] for i in range(0, len(sentences), 5 - token_overlap)]
    return chunks
