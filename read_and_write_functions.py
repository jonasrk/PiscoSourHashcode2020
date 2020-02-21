"read and write functions"

import sys

# import numpy as np

def compute_solution(n_books, n_libs, n_days, scores, libs):

    order_libs = []
    remaining_days = n_days

    used_libs = set([])
    books_sent = set([])
    score = 0

    while remaining_days > 0:
        best_next = -1
        best_next_score = -1
        best_next_signin = -1
        best_next_books = []
        for li in range(1, len(libs)):
            if li in used_libs:
                continue
            
            li_nbooks, li_signup, li_max, li_books, i, li_bookscore = libs[li]
            li_score = -1
            
            if (remaining_days - li_signup) <= 0:
                li_score = 0
            else:
                li_working_days = remaining_days - li_signup

                
                new_li_books = set(li_books)
                new_li_books = new_li_books.difference(books_sent)
                new_li_books = list(new_li_books)
                def bookscore(book_id):
                    return scores[book_id]
                new_li_books = sorted(new_li_books, reverse=True, key=bookscore)

                li_books_to_send = min(len(new_li_books), li_working_days*li_max)
                li_score = 0
                
                for bi in new_li_books[:li_books_to_send]:
                    li_score += scores[bi]

            if li_score > best_next_score:
                best_next = li
                best_next_score = li_score
                best_next_signin = li_signup
                best_next_books = new_li_books

                
        if best_next_score <= 0:
            break
        else:
            order_libs.append(best_next)
            used_libs.add(best_next)
            best_next_books = set(best_next_books)
            books_sent = books_sent.union(best_next_books)
            remaining_days -= best_next_signin
            score += best_next_score
    return order_libs, score

def compute_solution2(n_books, n_libs, n_days, scores, libs):

    order_libs = []
    remaining_days = n_days

    used_libs = set([])
    books_sent = set([])
    score = 0

    while remaining_days > 0:
        best_next = -1
        best_next_score = -1
        best_next_signin = -1
        best_next_books = []
        for li in range(1, len(libs)):
            if li in used_libs:
                continue
            
            li_nbooks, li_signup, li_max, li_books, i, li_bookscore = libs[li]
            li_score = -1
            
            if (remaining_days - li_signup) <= 0:
                li_score = 0
            else:
                li_working_days = remaining_days - li_signup

                
                new_li_books = set(li_books)
                new_li_books = new_li_books.difference(books_sent)
                new_li_books = list(new_li_books)
                def bookscore(book_id):
                    return scores[book_id]
                new_li_books = sorted(new_li_books, reverse=True, key=bookscore)

                li_books_to_send = min(len(new_li_books), li_working_days*li_max)
                li_score = 0
                
                for bi in new_li_books[:li_books_to_send]:
                    li_score += scores[bi]

            if li_score > best_next_score:
                best_next = li
                best_next_score = li_score
                best_next_signin = li_signup
                best_next_books = new_li_books

                
        if best_next_score <= 0:
            break
        else:
            order_libs.append(best_next)
            used_libs.add(best_next)
            best_next_books = set(best_next_books)
            books_sent = books_sent.union(best_next_books)
            remaining_days -= best_next_signin
            score += best_next_score
    return order_libs, score
        


def read_input_file(file_name):
    """
    Reads the input file and returns m, n and sizes
    """

    print(file_name)
    all_books = {}
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

            for book in li_books:
                if book not in all_books:
                    all_books[book] = 1
                else:
                    all_books[book] += 1

            def bookscore(bi):
                return scores[bi]

            li_books = sorted(li_books, reverse=True, key=bookscore)

            li_bookscore = 0
            for bi in li_books:
                li_bookscore += scores[bi]
            li_bookscore = li_bookscore / li_nbooks

            libs.append((li_nbooks, lui_signup, li_max, li_books, i, li_bookscore))

#    for lib_i in range(len(libs)):
#
#        def book_qual(book_id):
#            return scores[book_id] / all_books[book_id]
#
#        li_books = sorted(libs[lib_i][3], reverse=True, key=book_qual)
#        qual_sum = sum(libs[lib_i][3])
#        qual = qual_sum / len(libs[lib_i][3])
#        new_lib = (
#            libs[lib_i][0],
#            libs[lib_i][1],
#            libs[lib_i][2],
#            li_books,
#            libs[lib_i][4],
#            libs[lib_i][5],
#            qual,
#        )
#
#        libs[lib_i] = new_lib

    return n_books, n_libs, n_days, scores, libs


def write_file(output_file, sln):
    """
    write the output file for the passed pizza
    """
    with open(output_file, "w") as fout:
        # number of pizzas
        fout.write(sln)
    print("file: " + output_file + " was saved")


def write_solution(filename, libs, ordered_libs):
    big_solution_string = ""

    for li in ordered_libs:
        
        big_solution_string += str(libs[li][4]) + " "
        big_solution_string += str(len(libs[li][3])) + "\n"
        book_list_string = ""

        for book in libs[li][3]:
            book_list_string += str(book) + " "

        book_list_string = book_list_string[:-1]
        big_solution_string += book_list_string + "\n"

    new_solution = ""
    new_solution += str(len(ordered_libs)) + "\n" + big_solution_string

    write_file(filename, new_solution)

    return

def create_dummy_solution(n_books, n_libs, n_days, scores, libs):
    big_solution_string = ""

    sent_books = set([])
    nlib = 0
    current_day = 0
    for i in range(n_libs):
        days_left = n_days - current_day - libs[i][1]
        max_books_to_send = min(days_left * libs[i][2], libs[i][0])

        books_li = set(libs[i][3])

        books_to_send = books_li.difference(sent_books)

        books_to_send = list(books_to_send)
        books_to_send = books_to_send[:max_books_to_send]

        books_to_send = set(books_to_send)

        sent_books = sent_books.union(books_to_send)

        if len(books_to_send) == 0:
            continue

        current_day += libs[i][1]
        big_solution_string += str(libs[i][4]) + " "
        big_solution_string += str(len(books_to_send)) + "\n"
        book_list_string = ""

        for book in books_to_send:
            book_list_string += str(book) + " "

        book_list_string = book_list_string[:-1]
        big_solution_string += book_list_string + "\n"
        nlib += 1

    new_solution = ""
    new_solution += str(nlib) + "\n" + big_solution_string

    return new_solution


def lib_quality_score(lib):
    max_sending_days = n_days - lib[1]
    no_of_books_in_the_lib = lib[0]
    max_send_per_day = lib[2]
    average_book_score = lib[5]
    # return (
    #     min(no_of_books_in_the_lib, max_send_per_day * max_sending_days)
    #     * average_books_score
    # )
    #    return (max_sending_days, min(no_of_books_in_the_lib, max_send_per_day * max_sending_days)
    #            * average_books_score)
    # return (max_sending_days, max_send_per_day, no_of_books_in_the_lib)
    return (max_sending_days) 
    #return average_book_rare_score


def filter_libs(n_books, n_libs, n_days, scores, libs):

    sent_books = set([])
    nlib = 0
    current_day = 0
    for i in range(n_libs):
        days_left = n_days - current_day - libs[i][1]
        max_books_to_send = min(days_left * libs[i][2], libs[i][0])

        books_li = set(libs[i][3])

        books_to_send = books_li.difference(sent_books)

        books_to_send = list(books_to_send)
        books_to_send = books_to_send[:max_books_to_send]

        books_to_send = set(books_to_send)

        sent_books = sent_books.union(books_to_send)

        if len(books_to_send) == 0:
            continue

        current_day += libs[i][1]
        big_solution_string += str(libs[i][4]) + " "
        big_solution_string += str(len(books_to_send)) + "\n"
        book_list_string = ""

        for book in books_to_send:
            book_list_string += str(book) + " "

        book_list_string = book_list_string[:-1]
        big_solution_string += book_list_string + "\n"
        nlib += 1


def main():

    # Read the input file
    input_path = "./input_files/"
    output_path = "./output_files/"
    file_name = "a_example.txt"
    file_name = "b_read_on.txt"
    file_name = "c_incunabula.txt"
    #file_name = "d_tough_choices.txt"
    file_name = "e_so_many_books.txt"
    file_name = "f_libraries_of_the_world.txt"

    global n_days, scores
    n_books, n_libs, n_days, scores, libs = read_input_file(input_path + file_name)

    sorted_libs = sorted(libs, reverse=True, key=lib_quality_score)
    #    print(sorted_libs)

    ordered_libs, score = compute_solution(n_books, n_libs, n_days, scores, libs)

    output_file = output_path + file_name
    write_solution(output_file, libs, ordered_libs)

    print(ordered_libs, score)

#    sln = create_dummy_solution(n_books, n_libs, n_days, scores, sorted_libs)

#    output_file = output_path + file_name
#    write_file(output_file, sln)

    return


def xx():
    # Write output

    write_file(output_file, pizzas_to_order)


if __name__ == "__main__":
    main()

# Next is Simon
