from typing import List, Dict, Tuple

import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors


class Tokenizer:
    vocabulary = "en_core_web_sm"
    try:
        nlp = spacy.load(vocabulary)
    except OSError:
        print(f"Downloading spaCy vocabulary module: {vocabulary}")
        spacy.cli.download(vocabulary)
        nlp = spacy.load(vocabulary)

    def __call__(self, text: str) -> List[str]:
        return [
            token.lemma_ for token in self.nlp(text)
            if not token.is_stop and not token.is_punct
        ]


class TextMatcher:

    def __init__(self, training_data: Dict):
        lookup = {k: " ".join(v.values()) for k, v in training_data.items()}
        self.targets = tuple(lookup.keys())
        self.tfidf = TfidfVectorizer(
            ngram_range=(1, 3),
            tokenizer=Tokenizer(),
            max_features=5000,
        )
        self.knn = NearestNeighbors(n_neighbors=1, n_jobs=-1)
        training_vector = self.tfidf.fit_transform(lookup.values())
        self.knn.fit(training_vector.todense())
        self.baseline, _ = self._worker("")

    def _worker(self, user_input: str) -> Tuple[float, int]:
        vec = self.tfidf.transform([user_input])
        dist, idx = self.knn.kneighbors(vec.todense())
        return float(dist), int(idx)

    def __call__(self, user_input: str) -> str:
        dist, idx = self._worker(user_input)
        if dist != self.baseline:
            return self.targets[idx]
        else:
            return "No Match"
