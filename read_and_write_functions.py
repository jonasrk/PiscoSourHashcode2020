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

    # Read the input file
    input_path = "../input_data/"
    # file_name = "a_example.in"
    # file_name = "b_small.in"
    # file_name = "c_medium.in"
    # file_name = "d_quite_big.in"
    file_name = "e_also_big.in"

    [m, n, sizes] = read_input_file(input_path + file_name)
    ids_of_pizzas = np.arange(n)
    print("Maximum number of pizza slices to order:", m)
    print("Number of dierent types of pizza:", n)

    # Trivial solution 1: add pizzas in order until limit is reached
    nb_of_slices = 0
    pizzas_to_order = []
    total_slices = 0
    for i in range(n):
        if total_slices + sizes[i] < m:
            pizzas_to_order.append(i)
            total_slices += sizes[i]
        else:
            print("limit reached")
            break
    print("Total slices", total_slices)

    # Write output
    output_file = "../results/output_" + file_name
    write_file(output_file, pizzas_to_order)


if __name__ == "__main__":
    main()

# Next is Simon
