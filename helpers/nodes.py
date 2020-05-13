import networkx as nx
import numpy as np


def get_nodes_probabilities(graph):
    probabilities = []
    num_of_edges = nx.number_of_edges(graph)
    all_degrees = (2 * num_of_edges)
    for node in graph.nodes():
        degree = graph.degree(node)
        probability = degree / all_degrees
        probabilities.append(probability)
    return probabilities


def get_random_nodes(graph, probabilities, num_of_edges):
    targets = set()
    while len(targets) < num_of_edges:
        targets.add(np.random.choice(graph.nodes(), p=probabilities))
    return targets
