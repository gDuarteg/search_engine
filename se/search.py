from .query import parse_raw_query
from .rank import rank_documents
from .index import Index


def search(raw_query, index: Index, docs):
    query = parse_raw_query(raw_query)
    index_query = query.evaluate(index)
    ranked_index = rank_documents(query, docs, index_query, index)
    return [docs[k] for k in ranked_index]
