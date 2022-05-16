import csv_parser
import json_parser
import books_to_users

if __name__ == "__main__":
    users = json_parser.get_users('users.json')
    books = csv_parser.get_books('books.csv')
    users_w_books = books_to_users.give_books_to_users(users, books)
    books_to_users.write_users_to_json('result.json', users_w_books)
