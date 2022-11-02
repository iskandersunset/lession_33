import requests

from configuration import SERVICE_URL
from src.base_classes.response import Response

# resp = requests.get(SERVICE_URL)
#
# print(resp.json())


def test_getting_users_list():
    response = requests.get(SERVICE_URL)
    test_object = Response(response)
    test_object.assert_status_code(200)

# {
#     "meta": {
#         "pagination": {
#             "total": 3991,
#             "pages": 400,
#             "page": 1,
#             "limit": 10,
#             "links": {
#                 "previous": null,
#                 "current": "https://gorest.co.in/public/v1/users?page=1",
#                 "next": "https://gorest.co.in/public/v1/users?page=2"
#             }
#         }
#     },
#     "data": [
#         {
#             "id": 4061,
#             "name": "Menaka Mahajan",
#             "email": "mahajan_menaka@crooks-deckow.biz",
#             "gender": "male",
#             "status": "active"
#         },
#         {
#             "id": 4060,
#             "name": "Ajit Nambeesan",
#             "email": "nambeesan_ajit@smith-harvey.info",
#             "gender": "male",
#             "status": "inactive"
#         },
#         {
#             "id": 4059,
#             "name": "Trilochana Abbott",
#             "email": "trilochana_abbott@tillman.org",
#             "gender": "male",
#             "status": "active"
#         },
#         {
#             "id": 4058,
#             "name": "Gov. Jyotsana Mukhopadhyay",
#             "email": "mukhopadhyay_jyotsana_gov@considine.biz",
#             "gender": "male",
#             "status": "active"
#         },
#         {
#             "id": 4057,
#             "name": "Prasad Gupta PhD",
#             "email": "prasad_gupta_phd@sauer.net",
#             "gender": "female",
#             "status": "active"
#         },
#         {
#             "id": 4056,
#             "name": "Anurag Kaur CPA",
#             "email": "kaur_anurag_cpa@hackett-johns.io",
#             "gender": "male",
#             "status": "inactive"
#         },
#         {
#             "id": 4055,
#             "name": "Adwitiya Varma III",
#             "email": "varma_iii_adwitiya@hodkiewicz-pagac.co",
#             "gender": "male",
#             "status": "active"
#         },
#         {
#             "id": 4054,
#             "name": "Karunanidhi Gill",
#             "email": "karunanidhi_gill@quitzon-moore.name",
#             "gender": "male",
#             "status": "inactive"
#         },
#         {
#             "id": 4053,
#             "name": "Pres. Bhima Kocchar",
#             "email": "kocchar_bhima_pres@stehr-homenick.org",
#             "gender": "female",
#             "status": "inactive"
#         },
#         {
#             "id": 4052,
#             "name": "Tapan Bharadwaj",
#             "email": "bharadwaj_tapan@turcotte.name",
#             "gender": "female",
#             "status": "active"
#         }
#     ]
# }
