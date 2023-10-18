# Name: Reda Mohsen Reda
# Project Title: AI Search Algorithms Application
import networkx as nx
import matplotlib.pyplot as plt
from PIL import Image
import re


def get_input_graph(input_entry):
    """
     prompt the user for input of graph edges with weights, validate the input, and return a list of graph edges.

     this function ensures that the user-provided graph edges are correctly formatted as (node, node=weight),
     where 'node' can be any alphanumeric character, and 'weight' must be a non-negative integer. The input format
     should be 'edge1+edge2+edge3+...' where each 'edge' conforms to the format mentioned.

     args: 'edge1+edge2+edge3+...' where edge formated as (node, node=weight)

     returns: list of tuples: A list of graph edges represented as tuples, where each tuple consists of two nodes and
     a dictionary with the 'weight' attribute.

     example:
     >>> get_input_graph()
     enter edges with weights as (node,node=weight+node,node=weight): A, B=3+C, D=2
     [('A', 'B', {'weight': '3'}), ('C', 'D', {'weight': '2'})]

     """
    # get graph edges concatenated with '+' from the user
    input_graph_edges = input_entry.get().strip()
    # get a list of graph edges
    input_graph_edges = input_graph_edges.split("+")
    # create a list to store graph edges in a correct format
    graph_edges = []
    for edge in input_graph_edges:
        # check if the edge is in a correct format and append it the the list created
        if match := re.search(r"^(\w+)\s*,\s*(\w+)\s*=\s*(\d+)$", edge.strip(), re.IGNORECASE):
            graph_edges.append((match.group(1), match.group(2), {"weight": match.group(3)}))
        # if user enter invalid input, return to input graph edges again
        else:
            # Display a message box for invalid input
            raise ValueError("Invalid edges")
    # return list of graph edges
    if len(graph_edges) == len(input_graph_edges):
        return graph_edges


def get_graph(graph_edges: list):
    try:
        """
         create a directed graph from a list of graph edges.
    
         args:
         graph_edges (list of tuples): a list of graph edges represented as tuples,
         where each tuple consists of two nodes.
    
         returns:
         nx.DiGraph: a NetworkX Directed Graph object created from the provided graph edges.
    
         Example:
         >>> graph_edges = [('A', 'B', {'weight': '3'}), ('C', 'D', {'weight': '2'})]
         >>> get_graph(graph_edges)
         <networkx.classes.digraph.DiGraph object at 0x...>
    
         """
        # create an empty directed graph
        graph = nx.DiGraph()
        # add edges to the graph based on the provided list of graph_edges
        graph.add_edges_from(graph_edges)
        # return the resulting graph
        return graph
    except TypeError:
        pass


def bfs(graph: nx.DiGraph, start_node: str, goal_nodes: list):
    """
    perform Breadth-First Search (BFS) on a directed graph to find a path from the start node to one of the goal nodes.

    args:
    graph (nx.DiGraph): a NetworkX Directed Graph object.
    start_node (str): the starting node for BFS.
    goal_nodes (list): a list of nodes to reach using BFS.

    returns:
    tuple or None: a tuple containing the cost and path if a path is found; otherwise, returns None.

    example:
    >>> G = nx.DiGraph()
    >>> G.add_edges_from([('A', 'B', {'weight': 1}), ('A', 'C', {'weight': 2}), ('B', 'D', {'weight': 3})])
    >>> s_node = 'A'
    >>> g_nodes = ['D', 'C']
    >>> bfs(G, s_node, g_nodes)
    (1, ['A', 'B', 'D'])
    """
    # check if graph is empty
    if graph is None:
        raise ValueError("Empty graph")
    # check if start node is not in graph
    if not graph.has_node(start_node):
        raise ValueError(f"Start node {start_node} is not in graph")
    # check if a goal node is not in graph
    for node in goal_nodes:
        if not graph.has_node(node):
            raise ValueError(f"Goal node {node} is not in graph")
    # initialize a queue to store the current node, cost, and path
    fringe = [(start_node, 0, [start_node])]
    # create a set to keep track of visited nodes
    visited = set()
    while fringe:
        node, cost, path = fringe.pop(0)
        # if the current node is one of the goal nodes, return the cost and path to this goal node
        if node in goal_nodes:
            # return cost and path to this goal node
            return cost, path
        visited.add(node)
        # explore neighboring nodes
        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                new_cost = cost + int(graph[node][neighbor]['weight'])
                new_path = path + [neighbor]
                fringe.append((neighbor, new_cost, new_path))
    # if no path is found, return None
    return None, None


def dfs(graph: nx.DiGraph, start_node: str, goal_nodes: list):
    """
    perform Depth-First Search (DFS) on a directed graph to find a path from the start node to one of the goal nodes.

    args:
    graph (nx.DiGraph): a NetworkX Directed Graph object.
    start_node (str): the starting node for BFS.
    goal_nodes (list): a list of nodes to reach using BFS.

    returns:
    tuple or None: a tuple containing the cost and path if a path is found; otherwise, returns None.

    example:
    >>> G = nx.DiGraph()
    >>> G.add_edges_from([('A', 'B', {'weight': 1}), ('A', 'C', {'weight': 2}), ('B', 'D', {'weight': 3})])
    >>> s_node = 'A'
    >>> g_nodes = ['D', 'C']
    >>> dfs(G, s_node, g_nodes)
    (1, ['A', 'B', 'D'])
    """
    # check if graph is empty
    if graph is None:
        raise ValueError("Empty graph")
    # check if start node is not in graph
    if not graph.has_node(start_node):
        raise ValueError(f"Start node {start_node} is not in graph")
    # check if a goal node is not in graph
    for node in goal_nodes:
        if not graph.has_node(node):
            raise ValueError(f"Goal node {node} is not in graph")
    # initialize a queue to store the current node, cost, and path
    fringe = [(start_node, 0, [start_node])]
    # create a set to keep track of visited nodes
    visited = set()
    while fringe:
        node, cost, path = fringe.pop()
        # if the current node is one of the goal nodes, return the cost and path to this goal node
        if node in goal_nodes:
            # return cost and path to this goal node
            return cost, path
        visited.add(node)
        # explore neighboring nodes
        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                new_cost = cost + int(graph[node][neighbor]['weight'])
                new_path = path + [neighbor]
                fringe.append((neighbor, new_cost, new_path))
    # if no path is found, return None
    return None, None


def ucs(graph, start_node, goal_nodes):
    """
    perform Uniform Cost Search (UCS) on a directed graph to find the lowest cost path
    from the start node to the goal node.

    args:
    graph (nx.DiGraph): a NetworkX Directed Graph object with non-negative edge weights.
    start_node (str): the starting node for UCS.
    goal_node (str): the goal node to reach.

    returns:
    tuple or None: a tuple containing the cost and path if a path is found; otherwise, returns None.

    example:
    >>> G = nx.DiGraph()
    >>> G.add_weighted_edges_from([('A', 'B', 1), ('A', 'C', 2), ('B', 'D', 3), ('C', 'D', 1)])
    >>> s_node = 'A'
    >>> g_nodes = 'D'
    >>> ucs(G , s_node, g_nodes)
    (4, ['A', 'C', 'D'])
    """
    # check if graph is empty
    if graph is None:
        raise ValueError("Empty graph")
    # check if start node is not in graph
    if not graph.has_node(start_node):
        raise ValueError(f"Start node {start_node} is not in graph")
    # check if a goal node is not in graph
    for node in goal_nodes:
        if not graph.has_node(node):
            raise ValueError(f"Goal node {node} is not in graph")
    # initialize a list (fringe) to store the current node, cost, and path
    fringe = [(0, start_node, [start_node])]

    while fringe:
        # find the path with the minimum cost in the fringe
        min_index = min(range(len(fringe)), key=lambda i: fringe[i][0])
        cost, node, path = fringe.pop(min_index)

        if node in goal_nodes:
            # if we've reached the goal node, return the cost and path
            return cost, path

        # explore neighboring nodes
        for neighbor in graph.neighbors(node):
            new_cost = cost + int(graph[node][neighbor]['weight'])

            # check if this node has already been visited with a lower cost
            if all(new_cost >= c for c, _, _ in fringe):
                # If not, add it to the fringe
                new_path = path + [neighbor]
                fringe.append((new_cost, neighbor, new_path))

    # if no path is found, return None
    return None, None


def draw_graph(graph: nx.DiGraph, start_node: str, goal_nodes: list, path: list, cost: int, search_algo):
    """
     draw and show a directed graph with specific node and edge attributes, and save it as a PNG file.

     args:
     graph (nx.DiGraph): a NetworkX Directed Graph object.
     start_node (str): the starting node.
     goal_nodes (list): a list of goal nodes.
     path (list): a list of nodes representing the path.
     cost (int): the cost of the path.
     search_algo (str): the search algorithm used (e.g., "BFS").

     returns:
     None

     example:
     >>> G = nx.DiGraph()
     >>> G.add_edges_from([('A', 'B', {'weight': 1}), ('A', 'C', {'weight': 2}), ('B', 'D', {'weight': 3})])
     >>> s_node = 'A'
     >>> g_nodes = ['D']
     >>> e_path = ['A', 'B', 'D']
     >>> e_cost = 4
     >>> e_search_algo = "BFS"
     >>> draw_graph(G, s_node, g_nodes, e_path, e_cost, e_search_algo)

     """
    # close previous fig if any
    plt.close()
    # set a layout for the graph
    pos = nx.spring_layout(graph, seed=43)  # Seed layout for graph reproducibility
    # set the node colors (red for start node, green for goal nodes and light blue for the rest of nodes)
    node_colors = ['red' if node == start_node
                   else 'green' if node in goal_nodes
                   else 'lightblue' for node in graph.nodes]
    # set the edge color of the path in green and rest of edges in black
    edge_colors = ['orange' if (u, v) in zip(path, path[1:]) else 'black' for u, v in graph.edges]
    # draw the graph with labels as nodes
    nx.draw(graph, pos=pos, node_color=node_colors, node_size=500, edge_color=edge_colors, with_labels=True)
    # set edge labels with weights of edges
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    # draw edge labels
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    # set a title with the path and cost of the graph
    title = f"Path using {search_algo} is: "
    separator = " -> "
    title += separator.join(path) + "\n"
    title += f"Cost using {search_algo} is: {cost}"
    plt.suptitle(title.strip(), x=0.7, y=0.1, fontweight="bold")
    # save graph figure
    plt.savefig("graph.png")
    # show the figure
    plt.show()
    # Open and display the saved figure
    # img = Image.open("graph.png")
    # img.show()
