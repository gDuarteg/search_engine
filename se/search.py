from se.query import parse_json_query
from se.retrieve import retrieve
from se.rank import rank_documents


def search(raw_query, index, docs):
    query = parse_json_query(raw_query)
    index_query = query.evaluate(index)
    ranked_index = rank_documents(query, docs, index_query)
    return [docs[k] for k in ranked_index]
