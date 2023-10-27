import json
import random

import requests

from constants import CREATE_POST_URL, REGISTER_USER_URL, USER_LOGIN_URL

with open('bot_config.json', 'r') as config_file:
    config = json.load(config_file)


def get_users():
    users = requests.get(REGISTER_USER_URL).json()
    username_list = [name['username'] for name in users]
    return username_list


def create_user(number_of_users):

    for n in range(1, number_of_users + 1):
        username_list = get_users()
        username = f'User_{n}'
        while username in username_list:
            n += 1
            username = f'User_{n}'
        email = f'user_{n}@email.com'
        password = '123'  # can be changed to random password generator

        user_data = {
            "username": username,
            "email": email,
            "password": password,
        }
        requests.post(REGISTER_USER_URL, json=user_data)
        print(f"User {username} created successfully.")


def generate_user_token(username):
    user_data = {
        "username": username,
        "password": '123',
    }
    tokens = requests.post(USER_LOGIN_URL, json=user_data).json()
    user_data = {
        'username': username,
        'access_token': tokens.get('access'),
        'refresh_token': tokens.get('refresh'),
    }
    return user_data


def create_post():
    users_list = get_users()
    for username in users_list:
        user = generate_user_token(username)
        access_token = user['access_token']
        headers = {'authorization': f'Bearer {access_token}'}

        post_data = {
            'title': f'{username} title',
            'content': f'{username} content',
        }

        for i in range(random.randint(1, config['max_posts_per_user'])):
            requests.post(CREATE_POST_URL, headers=headers, json=post_data).json()


def like_post():
    users_list = get_users()
    for username in users_list:
        user = generate_user_token(username)
        access_token = user['access_token']
        headers = {'authorization': f'Bearer {access_token}'}

        get_posts = requests.get(CREATE_POST_URL, headers=headers).json()
        ids = [i['id'] for i in get_posts]

        for i in random.sample(ids, random.randint(1, len(ids))):
            like_url = f'http://localhost:8000/post/posts/{i}/like/'
            requests.get(like_url, headers=headers)


if __name__ == '__main__':
    create_user(config['number_of_users'])
    create_post()
    like_post()
