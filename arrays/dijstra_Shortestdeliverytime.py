import networkx as nx
import numpy as np
A = np.array([[0, 0, 122, 0],
              [0, 0, 0, 50],
              [341, 0, 0, 205],
              [456, 0, 186, 0]])
G = nx.from_numpy_matrix(A, create_using=nx.DiGraph())
# print(G.nodes())
# print(G.edges())
answer = nx.single_source_dijkstra_path_length(G,1)
if len(answer)==len(G.nodes()):
    delivery_time=sum(answer.values())
    print(delivery_time)
else:
    print('Null')