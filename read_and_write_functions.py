"read and write functions"

import sys
import numpy as np


def read_input_file(file_name):
    """
    Reads the input file and returns m, n and sizes
    """

    with open(file_name, "r") as fin:
        line = fin.readline()
        m, n = [int(num) for num in line.split()]
        line = fin.readline().split()
        sizes = np.empty(n)
        for i in range(n):
            sizes[i] = int(line[i])
    return m, n, sizes


def write_file(output_file, pizzas_to_order):
    """
    write the output file for the passed pizza
    """
    with open(output_file, "w") as fout:
        # number of pizzas
        fout.write("%d\n" % len(pizzas_to_order))
        for s in pizzas_to_order:
            fout.write(str(s) + " ")
    print("file: " + output_file + " was saved")


def main():
    data = read_input_file("./input_files/a_example.in")

    print(data)

    write_file("./output_files/a_example.out", [1, 1])


if __name__ == "__main__":
  main()