import json


def get_users(path):
    personal_info = []
    with open(path, 'r') as json_file:
        users = json.load(json_file)
        for user in users:
            user_info = {
                'name': user['name'],
                'gender': user['gender'],
                'address': user['address'],
                'age': user['age'],
                'books': []
            }
            personal_info.append(user_info)
    return personal_info
