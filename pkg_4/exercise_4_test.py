from pkg_4.exercise_4 import bipartite
from TdP_collections.graphs.graph import Graph


def test_bipartite_connected_verified():
    """
    Verifica che che bipartite() riconosca correttamente un grafo connesso bipartito
    :return:
    """
    B = Graph()
    v1 = B.insert_vertex(1)
    v2 = B.insert_vertex(2)
    v3 = B.insert_vertex(3)
    v4 = B.insert_vertex(4)
    v5 = B.insert_vertex(5)
    v6 = B.insert_vertex(6)
    v7 = B.insert_vertex(7)
    B.insert_edge(v1, v2, 3)
    B.insert_edge(v1, v4, 3)
    B.insert_edge(v2, v3, 5)
    B.insert_edge(v3, v4, 2)
    B.insert_edge(v4, v5, 5)
    B.insert_edge(v5, v6, 1)
    B.insert_edge(v5, v7, 1)
    e = B.edges()

    if bipartite(B) is None:
        print('Test test_bipartite_connected_verified failed')
    else:
        A, B = bipartite(B)
        C = set()
        D = set()
        for x in A:
            C.add(x.element())
        for y in B:
            D.add(y.element())
        print('Test test_bipartite_connected_verified passed')


def test_bipartite_connected_not_verified():
    """
    Verifica che che bipartite() riconosca correttamente un grafo connesso non bipartito
    :return:
    """
    B = Graph()
    v1 = B.insert_vertex(1)
    v2 = B.insert_vertex(2)
    v3 = B.insert_vertex(3)
    v4 = B.insert_vertex(4)
    v5 = B.insert_vertex(5)
    v6 = B.insert_vertex(6)
    v7 = B.insert_vertex(7)
    B.insert_edge(v1, v2, 3)
    B.insert_edge(v1, v4, 3)
    B.insert_edge(v2, v3, 5)
    B.insert_edge(v3, v4, 2)
    B.insert_edge(v4, v5, 5)
    B.insert_edge(v5, v6, 1)
    B.insert_edge(v5, v7, 1)

    # arco rotto
    B.insert_edge(v2, v4, 5)

    if bipartite(B) is None:
        print('Test test_bipartite_connected_not_verified passed')
    else:
        print('Test test_bipartite_connected_not_verified failed')


def test_bipartite_unconnected_verified():
    B = Graph()
    v1 = B.insert_vertex(1)
    v2 = B.insert_vertex(2)
    v3 = B.insert_vertex(3)
    v4 = B.insert_vertex(4)
    v5 = B.insert_vertex(5)
    v6 = B.insert_vertex(6)
    v7 = B.insert_vertex(7)
    B.insert_edge(v1, v2, 3)
    B.insert_edge(v1, v4, 3)
    B.insert_edge(v3, v2, 5)
    B.insert_edge(v3, v4, 2)

    B.insert_edge(v5, v6, 1)
    B.insert_edge(v5, v7, 1)
    e = B.edges()

    if bipartite(B) is None:
        print('Test test_bipartite_unconnected_verified failed')
    else:
        A, B = bipartite(B)
        C = set()
        D = set()
        for x in A:
            C.add(x.element())
        for y in B:
            D.add(y.element())
        print('Test test_bipartite_unconnected_verified passed')


def test_bipartite_unconnected_not_verified():
    B = Graph()
    v1 = B.insert_vertex(1)
    v2 = B.insert_vertex(2)
    v3 = B.insert_vertex(3)
    v4 = B.insert_vertex(4)
    v5 = B.insert_vertex(5)
    v6 = B.insert_vertex(6)
    v7 = B.insert_vertex(7)
    B.insert_edge(v1, v2, 3)
    B.insert_edge(v1, v4, 3)
    B.insert_edge(v3, v2, 5)
    B.insert_edge(v3, v4, 2)

    B.insert_edge(v5, v6, 1)
    B.insert_edge(v5, v7, 1)

    # arco rotto
    B.insert_edge(v2, v4, 2)

    if bipartite(B) is None:
        print('Test test_bipartite_unconnected_not_verified passed')
    else:
        print('Test test_bipartite_unconnected_not_verified failed')


def execute_test():
    test_bipartite_connected_verified()
    test_bipartite_connected_not_verified()
    test_bipartite_unconnected_verified()
    test_bipartite_unconnected_not_verified()


if __name__ == "__main__":
    execute_test()
