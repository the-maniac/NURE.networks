import networkx as nx
import numpy as np


def get_number_of_edges(L, graph):
    V = nx.number_of_nodes(graph)
    E = nx.number_of_edges(graph)
    delta_e = L * float(E) / float(V - 1)
    num1 = int(delta_e)
    num2 = int(delta_e) + 1
    probability = [delta_e - num1, num2 - delta_e]
    num_of_edges = np.random.choice([num1, num2], p=probability)
    return num_of_edges
