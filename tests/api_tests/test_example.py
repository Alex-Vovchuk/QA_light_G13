import requests
from jsonpath_ng.ext import parse
from jsonschema import validate

from src.jsonschemas.users_schemas import get_all_users
from src.services.users_service import UsersService

#
# def test_get_all():
#     session = requests.Session()
#     headers = {'Authorization': "Bearer sadfg34565zdfbsadfg"}
#     response = session.get("https://reqres.in/api/users", headers=headers, params={})
#


def test_create_item():
    user_service = UsersService()
    all_users = user_service.get_users_list()
    needed_user = get_parameter('$.data[?(@.id==5)]', all_users.json())
    needed_user_1 = [user_id['id'] for user_id in all_users.json()['data']]
    print(needed_user)
    print(needed_user_1)


    # my_user = {"name": "Apollo Green", "job": "Influencer"}
    # response = user_service.create_user(my_user)
    # all_users_after = user_service.get_users_list()
    # user_info = user_service.get_user(response.json())


def get_parameter(json_path, json_response):
    values = [match.value for match in parse(json_path).find(json_response)]
    return values


some = {
    "per_page": 6,
    "total": 12,
    "total_pages": 2,
    "data": [
        {
            "id": 7,
            "email": "michael.lawson@reqres.in",
            "first_name": "Michael",
            "last_name": "Lawson",
            "avatar": "https://reqres.in/img/faces/7-image.jpg"
        },
    ],
    "support": {
        "url": "https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral",
        "text": "Tired of writing endless social media content? Let Content Caddy generate it for you."
    }
}


def test_get_all_items():
    user_service = UsersService()
    all_users = user_service.get_users_list()

    all_users.validate_schema(get_all_users)


