import numpy


def get_percentages(matrix):
    """
    From a Weisfeiler-Lehman matrix result calculates the similarity percentages
    :param matrix: result of the Weisfeiler-Lehman algorithm
    :return: a matrix with the similarity percentages
    """
    percentages = matrix.copy()
    n = len(percentages)
    for i in range(n):
        for j in range(n):
            if i != j:
                percentages[i][j] = (percentages[i][j] / percentages[i][i]) * 100
    for i in range(n):
        percentages[i][i] = (percentages[i][i] / percentages[i][i]) * 100
    return percentages


def expand_isomorphism_matrix(isomorphism_data):
    """
    From a partial data list generates a matrix with the isomorphism data
    :param isomorphism_data: a list of uncompleted lists of boolean values indicating True if are isomorphic to other
    in the index or false in the other case
    :return: an expanded matrix
    """
    n = len(isomorphism_data)
    isomorphism_matrix = numpy.full((n, n), True)
    for i in range(len(isomorphism_data)):
        for j in range(len(isomorphism_data[i])):
            isomorphism_matrix[i][i + j + 1] = isomorphism_data[i][j]
    lower = numpy.tril_indices(n, -1)
    isomorphism_matrix[lower] = isomorphism_matrix.T[lower]
    return isomorphism_matrix


def is_isomorphic(graph, list_of_graphs):
    """
    Checks if a graph is isomorphic to a list of graphs
    :param graph: the graph to check if is isomorphic against a list of graphs
    :param list_of_graphs: the list of graphs
    :return: a list with boolean values indicating if the graph is isomorphic to the others
    """
    return [graph.isomorphic(tested) for tested in list_of_graphs]


def is_isomorphic_star(args):
    """
    Trick to use tqdm with parallel processing
    """
    return is_isomorphic(*args)
