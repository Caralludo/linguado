import copy
import numpy
import tqdm

from collections import defaultdict


def wl_subtree_kernel(graphs, h):
    """
    Calculates the Weisfeiler-Lehman matrix from a set of graphs
    :param graphs: list of graphs
    :param h: number the iterations of the algoritm
    :return: a matrix with the Weisfeiler-Lehman values between graphs
    """
    N = len(graphs)

    labels = {}
    label_lookup = {}

    for G in graphs:
        for node in G.nodes():
            G.nodes[node]['label'] = G.degree(node)

    orig_graph_map = {it: {i: defaultdict(lambda: 0) for i in range(N)} for it in range(-1, h)}

    # initial labeling
    ind = 0
    for G in graphs:
        labels[ind] = numpy.zeros(G.number_of_nodes(), dtype=numpy.int32)
        node2index = {}
        for node in G.nodes():
            node2index[node] = len(node2index)

        for node in G.nodes():
            label = G.nodes[node]['label']
            if not label in label_lookup:
                label_lookup[label] = len(label_lookup)

            labels[ind][node2index[node]] = label_lookup[label]
            orig_graph_map[-1][ind][label] = orig_graph_map[-1][ind].get(label, 0) + 1

        ind += 1

    compressed_labels = copy.deepcopy(labels)

    # WL iterations
    for it in tqdm.tqdm(range(h)):
        label_lookup = {}
        ind = 0
        for G in graphs:
            node2index = {}
            for node in G.nodes():
                node2index[node] = len(node2index)

            for node in G.nodes():
                node_label = tuple([labels[ind][node2index[node]]])
                neighbors = G.neighbors(node)
                if len(list(neighbors)) > 0:
                    neighbors_label = tuple([labels[ind][node2index[neigh]] for neigh in neighbors])
                    node_label = str(node_label) + "-" + str(sorted(neighbors_label))
                if not node_label in label_lookup:
                    label_lookup[node_label] = len(label_lookup)

                compressed_labels[ind][node2index[node]] = label_lookup[node_label]
                orig_graph_map[it][ind][node_label] = orig_graph_map[it][ind].get(node_label, 0) + 1

            ind += 1

        labels = copy.deepcopy(compressed_labels)

    K = numpy.zeros((N, N))
    for it in range(-1, h):
        for i in range(N):
            for j in range(N):
                common_keys = set(orig_graph_map[it][i].keys()) & set(orig_graph_map[it][j].keys())
                K[i][j] += sum([orig_graph_map[it][i].get(k, 0) * orig_graph_map[it][j].get(k, 0) for k in common_keys])
    return K
