# Name: Reda Mohsen Reda
# Project Title: AI Search Algorithms Application
import networkx as nx
import matplotlib.pyplot as plt
import re
import sys


def main():
    graph = get_graph(get_input_graph())
    cost_to_goal, path_to_goal = bfs(graph, "s", ["i", "g"])
    if path_to_goal is not None:
        print("Path:", *path_to_goal)
        print("Cost:", cost_to_goal)
    else:
        print("Failed to reach goal nodes")


def get_input_graph():
    """
     Prompt the user for input of graph edges with weights, validate the input, and return a list of graph edges.

     This function ensures that the user-provided graph edges are correctly formatted as (node, node=weight),
     where 'node' can be any alphanumeric character, and 'weight' must be a non-negative integer. The input format
     should be 'edge1+edge2+edge3+...' where each 'edge' conforms to the format mentioned.

     Returns: list of tuples: A list of graph edges represented as tuples, where each tuple consists of two nodes and
     a dictionary with the 'weight' attribute.

     Example:
     >>> get_input_graph()
     Enter edges with weights as (node,node=weight+node,node=weight): A, B=3+C, D=2
     [('A', 'B', {'weight': '3'}), ('C', 'D', {'weight': '2'})]

     """
    # infinite loop to make sure the input edges are correct
    while True:
        # get graph edges concatenated with '+' from the user
        input_graph_edges = input("Enter edges with weights as (node,node=weight+node,node=weight): ").strip()
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
                print("Invalid edges")
                break
        # return list of graph edges
        if len(graph_edges) == len(input_graph_edges):
            return graph_edges


def get_graph(graph_edges: list):
    try:
        if graph_edges is not None:
            graph = nx.DiGraph()
            graph.add_edges_from(graph_edges)
            return graph
        else:
            raise ValueError("Wrong graph edges")
    except ValueError:
        pass


def bfs(graph: nx.DiGraph, start_node: str, goal_nodes: list):
    try:
        # check if graph is empty
        if graph is None:
            raise ValueError("Empty graph")
        # check if start node is not in graph
        if not graph.has_node(start_node):
            raise ValueError("Start node is not in graph")
        # check if a goal node is not in graph
        for node in goal_nodes:
            if not graph.has_node(node):
                raise ValueError(f"Goal node {node} is not in graph")
        # store the current node, cost, and path in a queue
        fringe = [(start_node, 0, [start_node])]
        # create a list of visited nodes in graph
        visited = set()
        while fringe:
            node, cost, path = fringe.pop(0)
            if node in goal_nodes:
                draw_graph(graph, start_node, goal_nodes, path, cost, "BFS")
                return cost, path
            visited.add(node)
            for neighbor in graph.neighbors(node):
                if neighbor not in visited:
                    new_cost = cost + int(graph[node][neighbor]['weight'])
                    new_path = path + [neighbor]
                    fringe.append((neighbor, new_cost, new_path))
        return None, None
    except ValueError as err:
        sys.exit(err)


def draw_graph(graph: nx.DiGraph, start_node: str, goal_nodes: list, path: list, cost: int, search_algo):
    # set a layout for the graph
    pos = nx.spring_layout(graph, seed=43)  # Seed layout for graph reproducibility
    # set the node colors (red for start node, green for goal nodes and lightblue for the rest of nodes)
    node_colors = ['red' if node == start_node
                   else 'green' if node in goal_nodes
                   else 'lightblue' for node in graph.nodes]
    # set the edge color of the path in green and rest of edges in black
    edge_colors = ['green' if (u, v) in zip(path, path[1:]) else 'black' for u, v in graph.edges]
    # draw the graph with labels as nodes
    nx.draw(graph, pos=pos, node_color=node_colors, node_size=500, edge_color=edge_colors, with_labels=True)
    # set edge labels with weights of edges
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    # draw edge labels
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    # set a title with the path and cost of the graph
    title = f"Path using {search_algo} is: "
    for path_node in path:
        title += path_node + " "
    title += f"// Cost using {search_algo} is: " + str(cost)
    plt.suptitle(title.strip(), fontweight="bold")
    # save the graph in png format
    plt.savefig("graph.png")


if __name__ == "__main__":
    main()
