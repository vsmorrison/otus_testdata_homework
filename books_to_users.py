import json


def give_books_to_users(users, books):
    index = 0
    for book in books:
        while index < len(users):
            users[index]['books'].append(book)
            index += 1
            break
        if index == len(users):
            index = 0
    return users


def write_users_to_json(path, users):
    with open(path, 'w') as file:
        json.dump(users, file, indent=4)
