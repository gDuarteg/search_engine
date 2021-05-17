from __future__ import annotations

import re
import json

from .index import Index, clean_text


class Node:
    def evaluate(self, _index: Index):
        return set()

    def get_terms(self):
        return set()


class Term(Node):
    def __init__(self, term):
        super().__init__()
        self.term = term

    def evaluate(self, index: Index):
        return set(index.get(self.term))

    def get_terms(self):
        return set((self.term,))


class Operation(Node):
    def __init__(self, nodes: list[Node]):
        super().__init__()
        self.nodes = nodes

    def combine(self, result, new_results):
        return set()

    def evaluate(self, index: Index):
        result = self.nodes[0].evaluate(index)
        for node in self.nodes[1:]:
            result = self.combine(result, node.evaluate(index))
        return result

    def get_terms(self):
        result = set()
        for node in self.nodes:
            result |= node.get_terms()
        return result


class OpAnd(Operation):
    def __init__(self, nodes):
        super().__init__(nodes)

    def combine(self, result, new_results):
        return result & new_results


class OpOr(Operation):
    def __init__(self, nodes):
        super().__init__(nodes)

    def combine(self, result, new_results):
        return result | new_results


def build_query(query):
    node_type = query[0]

    if node_type == "term":
        # ["term", "abelha"]
        return Term(query[1])

    # ["and", ["term", "abelha"], ["term", "rainha"]]
    arg_list = []
    for arg in query[1:]:
        arg_node = build_query(arg)
        arg_list.append(arg_node)

    if node_type == "and":
        return OpAnd(arg_list)
    if node_type == "or":
        return OpOr(arg_list)
    raise KeyError(f"Operação {node_type} desconhecida.")


def parse_raw_query(query: str):
    and_list = []
    or_list = []

    pat_and = re.compile('(".+?")')

    # words = clean_text(query)
    for q in pat_and.split(query):
        if q == "":
            continue
        if q[0] == q[-1] == '"':
            q = q[1:-1]
            q = [w for w in clean_text(q).split() if w != ""]
            if len(q) == 1:
                and_list.append(q[0])
            else:
                and_list.append(q)
        else:
            for word in clean_text(q).split():
                if word != "":
                    or_list.append(word)

    res_or = [["term", word] for word in or_list]
    res_and = [
        ["term", word] if isinstance(word, str) else ["and"] + [["term", iword] for iword in word]
        for word in and_list
    ]

    and_len = len(and_list)
    or_len = len(or_list)

    if and_len == 1 and or_len == 0:
        res = res_and[0]

    elif and_len == 0 and or_len == 1:
        res = res_or[0]

    elif and_len >= 0:
        res = ["and"] + res_and
        if or_len >= 0:
            res += [["or"] + res_or]
    else:
        res = [["or"] + res_or]

    return build_query(res)


def parse_json_query(json_query: str):
    q = json.loads(json_query)
    query = build_query(q)
    return query
