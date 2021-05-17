import math

from .index import Index


def score_document(query, doc, doc_number, index: Index):
    N_docs = len(doc)

    score = 0
    for word in query:
        count = index.get_count(word, str(doc_number))

        if count != 0:
            w = index.get(word)
            score += math.log2(1 + count) * math.log2(N_docs / len(w))
    return score


def rank_documents(query, docs, index_query, index: Index):
    terms = query.get_terms()
    ranked_index = []
    for doc_number in index_query:
        doc_number = int(doc_number)
        doc = docs[doc_number]
        score = score_document(terms, doc, doc_number, index)
        ranked_index.append((score, doc_number))
    ranked_index = sorted(ranked_index, key=lambda x: -x[0])
    return [item[1] for item in ranked_index]
