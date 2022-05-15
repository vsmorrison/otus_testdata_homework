import csv_parser
import json_parser

if __name__ == "__main__":
    loaded_json = json_parser.load_json('users.json')
    personal_info = json_parser.get_personal_info(loaded_json)
    print(personal_info)
    books = csv_parser.get_books('books.csv')
    print(books)
