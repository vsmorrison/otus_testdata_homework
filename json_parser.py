import json


def load_json(path):
    with open(path, 'r') as json_file:
        users = json.load(json_file)
    return users


def get_personal_info(users):
    personal_info = []
    for user in users:
        user_info = {
            'name': user['name'],
            'gender': user['gender'],
            'address': user['address'],
            'age': user['age']
        }
        personal_info.append(user_info)
    return personal_info

