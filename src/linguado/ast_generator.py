import antlr4
import tqdm
from igraph import *


def get_labels(parser):
    """
    Generates a dictionary of node names and id's
    :param parser: the antlr4 parser of a language
    :return: dictionary of node names and id's
    """
    labels = {}
    for attribute in dir(parser):
        identifier = len(labels)
        labels[attribute] = identifier
    labels["TerminalNodeImpl"] = len(labels)
    return labels


def sources_to_igraph(sources, language, language_functions, labels):
    """
    Obtains the AST from a set of files
    :param sources: a list with the path of the files to be analyzed
    :param language: string with the language of the files
    :param language_functions: functions of the lexer and parser for each language
    :param labels: a dictionary with the names of the parser rules and id's
    :return: a list of graphs (one graph for each file)
    """
    result = []
    for source in tqdm.tqdm(sources):
        ast = source_to_igraph(source, language, language_functions, labels)
        result.append(ast)
    return result


def source_to_igraph(source, language, language_functions, labels):
    """
    Obtains the AST from a file
    :param source: path of the file to be analyzed
    :param language: string with the language of the file
    :param language_functions: functions of the lexer and parser for each language
    :param labels: a dictionary with the names of the parser rules and id's
    :return: a graph with the ast of the source
    """
    graph = Graph(directed=True)
    file = antlr4.FileStream(source, encoding="latin-1")
    lexer = language_functions[language][0](file)
    stream = antlr4.CommonTokenStream(lexer)
    parser = language_functions[language][1](stream)
    get_tree = getattr(parser, language_functions[language][2])
    tree = get_tree()
    ast_visit(graph, tree, labels)
    return graph


def ast_visit(graph, node, labels):
    """
    Converts an antlr4 tree to igraph.
    :param graph: igraph where the result will be stored
    :param node: antlr4 node
    :param labels: a dictionary with the names of the parser rules and id's
    :return: returns the vertex visited
    """
    vertex = graph.add_vertex(label=labels[type(node).__name__])
    if not isinstance(node, antlr4.tree.Tree.TerminalNode):
        for child in node.getChildren():
            descendant = ast_visit(graph, child, labels)
            graph.add_edge(vertex, descendant)
    return vertex
