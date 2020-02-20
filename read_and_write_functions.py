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
        n_books, n_libs, n_days = [int(num) for num in line.split()]
        line = fin.readline()

        scores = [int(num) for num in line.split()]

        libs = []
        for i in range(n_libs):
            line = fin.readline()
            li_nbooks, lui_signup, li_max = [int(num) for num in line.split()]
            line = fin.readline()
            li_books = [int(num) for num in line.split()]

            def bookscore(bi):
                return scores[bi]

            li_books = sorted(li_books, reverse = True, key = bookscore)
            
            li_bookscore = 0
            for bi in li_books:
                li_bookscore += scores[bi]

            libs.append((li_nbooks, lui_signup, li_max, li_books, i, li_bookscore))
    return n_books, n_libs, n_days, scores, libs


def write_file(output_file, sln):
    """
    write the output file for the passed pizza
    """
    with open(output_file, "w") as fout:
        # number of pizzas
        fout.write(sln)
    print("file: " + output_file + " was saved")


def create_dummy_solution(n_books, n_libs, n_days, scores, libs):
    big_solution_string = ""

    big_solution_string += str(n_libs) + "\n"

    for i in range(n_libs):
        big_solution_string += str(libs[i][4]) + " " + str(libs[i][0]) + "\n"
        book_list_string = ""
        for book in libs[i][3][:-1]:
            book_list_string += str(book) + " "
        book_list_string += str(libs[i][3][-1])
        big_solution_string += book_list_string + "\n"

    return big_solution_string


def sort_lib(lib):
    max_sending_days = n_days - lib[1]
    return - max(lib[0],lib[2]*max_sending_days)
    



def main():

    # Read the input file
    input_path = "./input_files/"
    output_path = "./output_files/"
    file_name = "a_example.txt"
    file_name = "b_read_on.txt"
    file_name = "c_incunabula.txt"
    file_name = "d_tough_choices.txt"
    file_name = "e_so_many_books.txt"
    file_name = "f_libraries_of_the_world.txt"

    n_books, n_libs, n_days, scores, libs = read_input_file(input_path + file_name)

    global n_days, scores
    sorted_libs = sorted(libs, key=sort_lib)
#    print(sorted_libs)

    sln = create_dummy_solution(n_books, n_libs, n_days, scores, sorted_libs)

    output_file = output_path + file_name
    write_file(output_file, sln)

    return


def xx():
    # Write output

    write_file(output_file, pizzas_to_order)


if __name__ == "__main__":
    main()

# Next is Simon
