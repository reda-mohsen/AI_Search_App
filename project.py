import networkx as nx
import matplotlib.pyplot as plt
import re
import sys

def main():
    input_graph_edges = get_input_graph()
    graph = get_graph(input_graph_edges)
    if bfs(graph,"s","g") is not None:
        print("Path:", *bfs(graph,"s","g"))
    else:
        print("Failed to reach path")

def bfs(graph, start_node, goal_node):
    if graph.__len__() < 1:
        raise ValueError("Empty graph")
    if not graph.has_node(start_node):
        raise ValueError("Start node is not in graph")
    if not graph.has_node(goal_node):
        raise ValueError("Goal node is not in graph")
    # create a queue
    fringe = []
    # create a list for visited nodes
    visited = []
    # create color map for nodes
    color_map = []
    visited.append(start_node)
    fringe.append(start_node)
    color_map.append('red')
    while fringe:
        start_node = fringe.pop(0)
        for node in graph.successors(start_node):
            color_map.append('blue')
            if node not in visited:
                fringe.append(node)
                visited.append(node)
            if node == goal_node:
                color_map[-1]='green'
                pos = nx.spring_layout(graph, seed=47)  # Seed layout for reproducibility
                nx.draw(graph,pos=pos,node_color=color_map,edge_color='grey', with_labels = True)
                for node in visited:
                    title += node + " "
                plt.suptitle(title.split(), fontweight ="bold")
                plt.savefig("graph.png")
                return visited
    return

def get_input_graph():
    try:
        graph_edges = []
        while True:
            print("Press ctrl+d to stop")
            input_graph = input("Edge (as Node, Node): ")
            if match := re.search(r"^(\w+)\, ?(\w+)", input_graph, re.IGNORECASE):
                graph_edges.append((match.group(1), match.group(2)))
            else:
                print("Invalid Format")
                continue

    except EOFError:
        print()
        return graph_edges

def get_graph(graph_edges: list):
    try:
        if len(graph_edges) != 0:
            graph = nx.DiGraph()
            graph.add_edges_from(graph_edges, color="red")
            return graph
        else:
            raise ValueError("Empty graph")
    except ValueError as err:
        sys.exit(err)

if __name__ == "__main__":
    main()