import requests

from configuration import SERVICE_URL
from src.base_classes.response import Response
from src.scheme.user import User


# resp = requests.get(SERVICE_URL)
# print(resp.__getstate__())
# print(resp.json())


# def test_getting_users_list(say_hello):
#     response = requests.get(SERVICE_URL)
#     test_object = Response(response)
#     test_object.assert_status_code(200).validate(User)

def test_getting_users_list(get_users):
    Response(get_users).assert_status_code(200).validate(User)
