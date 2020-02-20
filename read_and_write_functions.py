"read and write functions"

import sys
import numpy as np


def read_input_file(file_name):
    """
    Reads the input file and returns m, n and sizes
    """

    print(file_name)
    with open(file_name, "r") as fin:
        line = fin.readline()
        n_books, n_libs, n_days = [int(num) for num in line.split(" ")]
        line = fin.readline()

        scores = [int(num) for num in line.split(" ")]

        libs = []
        for i in range(n_libs):
            line = fin.readline()
            li_nbooks, lui_signup, li_max = [int(num) for num in line.split(" ")]
            line = fin.readline().split()
            li_books = [int(num) for num in line.split(" ")]

            libs.append((li_nbooks, lui_signup, li_max, li_books))
    return n_books, n_libs, n_days, scores, libs


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

    # Read the input file
    input_path = "./input_files/"
    file_name = "a_example.txt"
    # file_name = "b_small.in"
    # file_name = "c_medium.in"
    # file_name = "d_quite_big.in"
    # file_name = "e_also_big.in"

    n_books, n_libs, n_days, scores, libs = read_input_file(input_path + file_name)
    print(n_books, n_libs, n_days, scores, libs)
    return

def xx():
    # Write output
    output_file = "../results/output_" + file_name
    write_file(output_file, pizzas_to_order)


if __name__ == "__main__":
    main()

# Next is Simon
