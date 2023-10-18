# Name: Reda Mohsen Reda
# Project Title: AI Search Algorithms Application
import tkinter as tk
import graph as g
from tkinter import messagebox

# Create a main application window
root = tk.Tk()
root.title("AI Search Application")
# Create a Frame to hold the Entry widget
frame_input = tk.Frame(root, padx=10, pady=10)
frame_input.pack(side="top")
frame_output = tk.Frame(root, padx=10, pady=10)
frame_output.pack()

# Create a label widget
input_edges_label = tk.Label(frame_input, text="Enter edges with weights as (node,node=weight+node,node=weight): ", padx=10, pady=10)
# Add the label widget to the window
input_edges_label.pack()
# Create an Entry widget within the Frame to get input edges
input_edges_entry = tk.Entry(frame_input, width=100)
input_edges_entry.pack()

# Create a label widget
input_start_node_label = tk.Label(frame_input, text="Enter start node: ", padx=10, pady=10)
# Add the label widget to the window
input_start_node_label.pack()
# Create an Entry widget within the Frame to get start node
start_node_entry = tk.Entry(frame_input, width=10)
start_node_entry.pack()

# Create a label widget
input_goal_nodes_label = tk.Label(frame_input, text="Enter goal nodes as (A,B,C,...): ", padx=10, pady=10)
# Add the label widget to the window
input_goal_nodes_label.pack()
# Create an Entry widget within the Frame to get goal nodes
goal_nodes_entry = tk.Entry(frame_input, width=30)
goal_nodes_entry.pack()

# Create a label widget
input_search_algorithm_label = tk.Label(frame_input, text="Select search algorithm: ", padx=10, pady=10)
# Add the label widget to the window
input_search_algorithm_label.pack()
# Create an Option Menu Widget with search algorithms
options = ["BFS", "DFS", "UCS"]
selected_option = tk.StringVar()
selected_option.set(options[0])  # Set the default option
option_var = tk.StringVar()
option_menu = tk.OptionMenu(frame_input, option_var, *options)
option_menu.pack()
# Set the default value in the OptionMenu
option_var.set(selected_option.get())

# Create a margin between the OptionMenu and the Button
tk.Label(frame_input, text="").pack()

# Create a margin between the Button and the Output
tk.Label(frame_input, text="").pack()
tk.Label(frame_input, text="").pack()

def output(cost_to_goal, path_to_goal):
    # Create a label widget
    path_to_goal_label = tk.Label(frame_output, text="Path to goal: ", padx=10, pady=10)
    # Add the label widget to the window
    path_to_goal_label.grid(row=0, column=0)
    # Create a label widget
    separator = " -> "
    path_to_goal = tk.Label(frame_output, text=separator.join(path_to_goal), padx=10, pady=10)
    # Add the label widget to the window
    path_to_goal.grid(row=0, column=1)

    # Create a label widget
    cost_to_goal_label = tk.Label(frame_output, text="Cost to goal: ", padx=10, pady=10)
    # Add the label widget to the window
    cost_to_goal_label.grid(row=1, column=0)
    # Create a label widget
    cost_to_goal = tk.Label(frame_output, text=cost_to_goal, padx=10, pady=10)
    # Add the label widget to the window
    cost_to_goal.grid(row=1, column=1)

def on_button_selected():
    try:
        # call functions in graph.py to build the graph with provided graph edges
        graph_edges = g.get_input_graph(input_edges_entry.get())
        graph = g.get_graph(graph_edges)

        # getting the start node from the user
        if start_node_entry.get():
            start_node = start_node_entry.get()
        else:
            raise ValueError("Empty start node")

        # getting the goal nodes from the user and put the nodes in a list
        if goal_nodes_entry.get():
            goal_nodes = []
            input_goal_nodes = goal_nodes_entry.get().split(",")
            for node in input_goal_nodes:
                goal_nodes.append(node.strip())
        else:
            raise ValueError("Empty goal nodes")

        selected_option.set(option_var.get())
        selected_algorithm = selected_option.get()
        if selected_algorithm == "BFS":
            cost_to_goal, path_to_goal = g.bfs(graph, start_node, goal_nodes)
            if path_to_goal:
                output(cost_to_goal, path_to_goal)
                g.draw_graph(graph, start_node, goal_nodes, path_to_goal, cost_to_goal, selected_algorithm)
            else:
                raise ValueError("Cannot reach path")
        elif selected_algorithm == "DFS":
            cost_to_goal, path_to_goal = g.dfs(graph, start_node, goal_nodes)
            if path_to_goal:
                output(cost_to_goal, path_to_goal)
                g.draw_graph(graph, start_node, goal_nodes, path_to_goal, cost_to_goal, selected_algorithm)
            else:
                raise ValueError("Cannot reach path")
        elif selected_algorithm == "UCS":
            cost_to_goal, path_to_goal = g.ucs(graph, start_node, goal_nodes)
            if path_to_goal:
                output(cost_to_goal, path_to_goal)
                g.draw_graph(graph, start_node, goal_nodes, path_to_goal, cost_to_goal, selected_algorithm)
            else:
                raise ValueError("Cannot reach path")

    except ValueError as value_err:
        print(value_err)
        messagebox.showerror("Error", value_err)
        pass
    except TypeError as type_err:
        print(type_err)
        messagebox.showerror("Error", type_err)
        pass

# Create a Button widget within the Frame to start search
button = tk.Button(frame_input, text="Search", padx=30, command=on_button_selected)
button.pack()

# Start the main event loop
root.mainloop()