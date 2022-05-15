import csv_parser
import json_parser

if __name__ == "__main__":
    users = json_parser.get_users('users.json')
    print(users)
    books = csv_parser.get_books('books.csv')
    print(books)
