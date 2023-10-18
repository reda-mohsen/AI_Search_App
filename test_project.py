import pytest
import networkx as nx
from graph import get_input_edges, get_graph, bfs, dfs, ucs


def test_get_input_graph():
    assert get_input_edges("A, B=3+C, D=2") == [('A', 'B', {'weight': '3'}), ('C', 'D', {'weight': '2'})]
    with pytest.raises(ValueError):
        get_input_edges("")
        get_input_edges("A,B=1 - A,C=4")
        get_input_edges("A B = 1 + A,C=4")
        get_input_edges("A B - 1 + A,C=4")


def test_get_graph():
    graph_edges = [('A', 'B', {'weight': '3'}), ('C', 'D', {'weight': '2'})]
    expected_graph = nx.DiGraph()
    expected_graph.add_edges_from(graph_edges)
    graph = get_graph(graph_edges)
    assert graph.edges == expected_graph.edges
    with pytest.raises(ValueError):
        get_graph("")


def test_bfs():
    graph = nx.DiGraph()
    graph.add_edges_from([('A', 'B', {'weight': '1'}), ('A', 'C', {'weight': '2'}), ('B', 'D', {'weight': '3'})])
    start_node = 'A'
    goal_nodes = ['D']
    cost, path = bfs(graph, start_node, goal_nodes)
    assert cost == 4
    assert path == ['A', 'B', 'D']
    graph = nx.DiGraph()
    with pytest.raises(ValueError):
        start_node = ""
        bfs(graph, start_node, goal_nodes)
        start_node = 'A'
        goal_nodes = ['']
        bfs(graph, start_node, goal_nodes)


if __name__ == '__main__':
    pytest.main()