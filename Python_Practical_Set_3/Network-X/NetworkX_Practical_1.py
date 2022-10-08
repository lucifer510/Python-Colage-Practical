# Draw this graph and apply following operation
# 1. Print total number of nodes.
# 2. Print total number of edges.
# 3. Print list of all the nodes.
# 4. Print list of all the edges.
# 5. Print in-degree for all the nodes.
# 6. Print out-degree for all the nodes.
# 7. Print successor of node 2.
# 8. Print predecessor of node 2.

import matplotlib.pyplot as plt
import networkx as nx

G = nx.DiGraph()  # Create a directed graph
G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8])
G.add_edges_from([(1, 2), (1, 4), (2, 3), (3, 4), (4, 8), (5, 1), (5, 7), (6, 5), (8, 3)])

nx.draw(G, with_labels=True)
plt.show()
print("Total number of nodes:", G.number_of_nodes())
print("Total number of edges:", G.number_of_edges())
print("List of all the nodes:", list(G.nodes))
print("List of all the edges:", list(G.edges))
print("In-degree for all the nodes:", G.in_degree())
print("Out-degree for all the nodes:", G.out_degree())
print("Successor of node 2:", list(G.successors(2)))
print("Predecessor of node 2:", list(G.predecessors(2)))
