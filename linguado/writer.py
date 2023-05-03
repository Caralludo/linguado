import csv
import numpy


def write_matrix(matrix, analyzed_files, path):
    files_column = [[file] for file in analyzed_files]
    result = numpy.hstack((files_column, matrix))

    files_row = analyzed_files.copy()
    files_row.insert(0, "")

    result = numpy.vstack((files_row, result))

    with open(path, "w", newline='') as file:
        writer = csv.writer(file)
        for row in result:
            writer.writerow(row)
