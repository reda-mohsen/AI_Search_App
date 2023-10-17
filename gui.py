import tkinter as tk
import project as p

# graph = p.get_graph(p.get_input_graph())
# cost_to_goal, path_to_goal = p.bfs(graph, "s", ["i", "g"])
# if path_to_goal is not None:
#     print("Path:", *path_to_goal)
#     print("Cost:", cost_to_goal)
# else:
#     print("Failed to reach goal nodes")

# Create a main application window
root = tk.Tk()
root.title("AI Search Application")
# Create a Frame to hold the Entry widget
frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

# Create a label widget
input_edges_label = tk.Label(frame, text="Enter edges with weights as (node,node=weight+node,node=weight): ", padx=10, pady=10)
# Add the label widget to the window
input_edges_label.pack()
# Create an Entry widget within the Frame to get input edges
input_edges_entry = tk.Entry(frame, width=100)
input_edges_entry.pack()
# Create a label widget
input_start_node_label = tk.Label(frame, text="Enter start node: ", padx=10, pady=10)
# Add the label widget to the window
input_start_node_label.pack()
# Create an Entry widget within the Frame to get start node
start_node_entry = tk.Entry(frame, width=10)
start_node_entry.pack()
# Create a label widget
input_goal_nodes_label = tk.Label(frame, text="Enter goal nodes as (A,B,C,...): ", padx=10, pady=10)
# Add the label widget to the window
input_goal_nodes_label.pack()
# Create an Entry widget within the Frame to get goal nodes
goal_nodes_entry = tk.Entry(frame, width=30)
goal_nodes_entry.pack()

# Create a label widget
input_search_algorithm_label = tk.Label(frame, text="Select search algorithm: ", padx=10, pady=10)
# Add the label widget to the window
input_search_algorithm_label.pack()
# Create an Option Menu Widget with search algorithms
options = ["BFS", "Option 2", "Option 3", "Option 4"]
selected_option = tk.StringVar()
selected_option.set(options[0])  # Set the default option
option_var = tk.StringVar()
option_menu = tk.OptionMenu(frame, option_var, *options)    # command=on_option_selected
option_menu.pack()
# Set the default value in the OptionMenu
option_var.set(selected_option.get())

# Create a Button widget within the Frame to start search
button = tk.Button(frame, text="Search", padx=10)   # command=on_button_selected
button.pack()
# entry.get() # to get input graph edges


# Start the main event loop
root.mainloop()