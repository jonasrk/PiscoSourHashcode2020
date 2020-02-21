import numpy as np


def read_input_file(file_name):
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

            li_books = sorted(li_books, reverse=True, key=bookscore)
            li_scores_of_books = []
            li_bookscore = 0
            for bi in li_books:
                li_bookscore += scores[bi]
                li_scores_of_books.append(scores[bi])
            li_bookscore = li_max * (li_bookscore / li_nbooks)

            libs.append(
                [
                    li_nbooks,
                    lui_signup,
                    li_max,
                    li_books,
                    i,
                    li_bookscore,
                    li_scores_of_books,
                ]
            )
    return n_books, n_libs, n_days, scores, libs


def write_file(output_file, sln):
    with open(output_file, "w") as fout:
        fout.write(sln)
    print("file: " + output_file + " was saved")
