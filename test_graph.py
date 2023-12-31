# ------------------------------------------
# Name: Reda Mohsen Reda
# Location: Egypt, Cairo
# Project Title: AI Search Algorithms
# Description:
# This application implements various search algorithms to find paths between a start node and goal node.
# The search algorithms implemented are:
#   - Breadth-First Search
#   - Depth-First Search
#   - Uniform-Cost Search
#   - Greedy Best-First Search
#   - A* Best-First Search
# ------------------------------------------
import pytest
import networkx as nx
from graph import get_input_edges, get_graph, bfs, dfs, ucs, greedy_search, a_star


def test_get_input_edges():
    assert get_input_edges("A, B=3+C, D=2") == [('A', 'B', {'weight': 3}), ('C', 'D', {'weight': 2})]
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
        get_graph([])


def test_bfs():
    graph = nx.Graph()
    graph.add_edges_from([('A', 'B', {'weight': '1'}), ('A', 'C', {'weight': '2'}), ('B', 'D', {'weight': '3'})])
    start_node = 'A'
    goal_nodes = ['D']
    cost, path = bfs(graph, start_node, goal_nodes)
    assert cost == 4
    assert path == ['A', 'B', 'D']
    graph = nx.Graph()
    with pytest.raises(ValueError):
        start_node = ""
        bfs(graph, start_node, goal_nodes)
        start_node = 'A'
        goal_nodes = ['']
        bfs(graph, start_node, goal_nodes)


def test_dfs():
    graph = nx.Graph()
    graph.add_edges_from([('A', 'B', {'weight': 1}), ('A', 'C', {'weight': 2}), ('B', 'D', {'weight': 3})])
    start_node = 'A'
    goal_nodes = ['D', 'C']
    cost, path = dfs(graph, start_node, goal_nodes)
    assert cost == 2
    assert path == ['A', 'C']
    graph = nx.DiGraph()
    with pytest.raises(ValueError):
        start_node = ""
        dfs(graph, start_node, goal_nodes)
        start_node = 'A'
        goal_nodes = ['']
        dfs(graph, start_node, goal_nodes)


def test_ucs():
    graph = nx.Graph()
    graph.add_edges_from([('A', 'B', {'weight': 1}), ('A', 'C', {'weight': 2}),
                          ('B', 'D', {'weight': 3}), ('C', 'D', {'weight': 3})])
    start_node = 'A'
    goal_nodes = ['D']
    cost, path = ucs(graph, start_node, goal_nodes)
    assert cost == 4
    assert path == ['A', 'B', 'D']
    graph = nx.DiGraph()
    with pytest.raises(ValueError):
        start_node = ""
        ucs(graph, start_node, goal_nodes)
        start_node = 'A'
        goal_nodes = ['']
        ucs(graph, start_node, goal_nodes)

def test_greedy():
    graph = nx.Graph()
    graph.add_edges_from([('A', 'B', {'weight': 1}), ('A', 'C', {'weight': 2}),
                          ('B', 'D', {'weight': 3}), ('C', 'D', {'weight': 3}),
                          ('B', 'E', {'weight': 1}), ('C', 'E', {'weight': 1})])
    start_node = 'A'
    goal_nodes = ['D', 'E']
    cost, path = greedy_search(graph, start_node, goal_nodes)
    assert cost == 2
    assert path == ['A', 'B', 'E']
    graph = nx.Graph()
    with pytest.raises(ValueError):
        start_node = ""
        greedy_search(graph, start_node, goal_nodes)
        start_node = 'A'
        goal_nodes = ['']
        greedy_search(graph, start_node, goal_nodes)

def test_a_star():
    graph = nx.Graph()
    graph.add_edges_from([('A', 'B', {'weight': 1}), ('A', 'C', {'weight': 2}),
                          ('B', 'D', {'weight': 3}), ('C', 'D', {'weight': 3}),
                          ('B', 'E', {'weight': 1}), ('C', 'E', {'weight': 1})])
    start_node = 'A'
    goal_nodes = ['D', 'E']
    cost, path = a_star(graph, start_node, goal_nodes)
    assert cost == 4
    assert path == ['A', 'B', 'D']
    graph = nx.Graph()
    with pytest.raises(ValueError):
        start_node = ""
        a_star(graph, start_node, goal_nodes)
        start_node = 'A'
        goal_nodes = ['']
        a_star(graph, start_node, goal_nodes)


if __name__ == '__main__':
    pytest.main()
