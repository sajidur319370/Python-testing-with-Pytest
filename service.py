import requests
import pytest

users = {1: "Alice", 2: "Bob", 3: "Horminee"}


def get_user(user_id):
    return users.get(user_id)


def get_users_from_api():
    res = requests.get("https://jsonplaceholder.typicode.com/users")
    if res.status_code == 200:
        return res.json()
    raise requests.HTTPError("Data is not fetched....")
