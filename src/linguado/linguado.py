import argparse
import itertools
import multiprocessing
import numpy
import tqdm

from linguado.ast_generator import get_labels
from linguado.graph_calculations import get_percentages, is_isomorphic_star, expand_isomorphism_matrix
from linguado.sample_generator import generate_sample_star
from linguado.weisfeiler_lehman import wl_subtree_kernel
from linguado.writer import write_matrix

from linguado.c.CLexer import CLexer
from linguado.c.CParser import CParser
from linguado.javascript.JavaScriptLexer import JavaScriptLexer
from linguado.javascript.JavaScriptParser import JavaScriptParser
from linguado.php.PhpLexer import PhpLexer
from linguado.php.PhpParser import PhpParser
from linguado.nasm_x86_64.nasm_x86_64_Lexer import nasm_x86_64_Lexer
from linguado.nasm_x86_64.nasm_x86_64_Parser import nasm_x86_64_Parser
from linguado.python2.Python2Lexer import Python2Lexer
from linguado.python2.Python2Parser import Python2Parser
from linguado.python3.Python3Lexer import Python3Lexer
from linguado.python3.Python3Parser import Python3Parser
from linguado.vba.vbaLexer import vbaLexer
from linguado.vba.vbaParser import vbaParser


def linguado():
    language_functions = {
        "c": [CLexer, CParser, "translationUnit"],
        "javascript": [JavaScriptLexer, JavaScriptParser, "program"],
        "php": [PhpLexer, PhpParser, "htmlDocument"],
        "nasm": [nasm_x86_64_Lexer, nasm_x86_64_Parser, "program"],
        "python2": [Python2Lexer, Python2Parser, "file_input"],
        "python3": [Python3Lexer, Python3Parser, "file_input"],
        "vba": [vbaLexer, vbaParser, "startRule"]
    }
    parser = argparse.ArgumentParser(
        description="Linguado is a tool which compares the AST of two or more files. Created by Guzmán Cernadas Pérez (@DonCaralludo) working for BE:SEC (@BESEC_byEmetel)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "files",
        metavar='Files',
        type=str,
        help="Files to analyze",
        nargs="+"
    )
    parser.add_argument(
        "language",
        metavar="Language",
        type=str,
        help="Language of the files. Options: " + ", ".join(language_functions.keys()),
        choices=language_functions.keys()
    )
    parser.add_argument(
        "-p",
        "--par",
        type=int,
        help="Changes the number of iterations of the Weisfeiler-Lehman algorithm",
        required=False,
        default=3
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        help="Changes the base name of the output files",
        required=False,
        default="result.csv"
    )
    args = parser.parse_args()

    labels = get_labels(language_functions[args.language][1])

    print("Generating AST's")
    inputs = zip(
        args.files,
        itertools.repeat(args.language),
        itertools.repeat(language_functions),
        itertools.repeat(labels)
    )
    with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
        samples = list(tqdm.tqdm(pool.imap_unordered(generate_sample_star, inputs), total=len(args.files)))

    samples.sort(key=lambda x: x.name)
    filenames = [sample.name for sample in samples]
    graphs = [sample.ast for sample in samples]

    print("Calculating Weisfeiler-Lehman matrix")
    nx_graphs = [g.to_networkx() for g in graphs]
    wl_matrix = wl_subtree_kernel(nx_graphs, h=args.par)
    wl_percentages = get_percentages(wl_matrix)

    print("Checking isomorphism (igraph)")
    inputs = []
    for i in range(len(graphs)):
        inputs.append((graphs[i], graphs[i + 1:]))
    with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
        isomorphism_data = list(tqdm.tqdm(pool.imap(is_isomorphic_star, inputs), total=len(args.files)))

    isomorphism_matrix = expand_isomorphism_matrix(isomorphism_data)

    print("Weisfeiler-Lehman:")
    print(wl_matrix)
    print("Weisfeiler-Lehman (%):")
    print(wl_percentages)
    wl_mean = numpy.mean(wl_matrix)
    wl_std_deviation = numpy.std(wl_matrix)
    wl_std_deviation_over_one = wl_std_deviation / wl_mean
    print("Mean:", wl_mean, ", Standard deviation: +-", wl_std_deviation, ", ", wl_std_deviation_over_one)
    print("Isomorphism test (igraph):")
    print(isomorphism_matrix)

    write_matrix(wl_matrix, filenames, "./wl_" + args.output)
    write_matrix(isomorphism_matrix, filenames, "./isomorphism_" + args.output)
