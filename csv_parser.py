import csv


def get_books(path):
    books_info = []
    with open(path, newline='') as csv_file:
        books = csv.DictReader(csv_file)
        for book in books:
            book_info = {
                "title": book['Title'],
                "author": book['Author'],
                "pages": book['Pages'],
                "genre": book['Genre']
            }
            books_info.append(book_info)
    return books_info
