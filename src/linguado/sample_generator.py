from linguado.sample import Sample
from linguado.ast_generator import source_to_igraph


def generate_sample(file, language, language_functions, labels):
    """
    Generates a sample from a path.
    :param file: path to a source code file
    :param language: language of the file
    :param language_functions: functions of the lexer and parser for each language
    :param labels: a dictionary with the names of the parser rules and id's
    :return: sample class instance
    """
    graph = source_to_igraph(file, language, language_functions, labels)
    sample = Sample(file, graph)
    return sample


def generate_sample_star(args):
    """
    Trick to use tqdm with parallel processing
    """
    return generate_sample(*args)
