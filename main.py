import requests


BASE_URL = 'https://f3e7328c-57f5-4d06-b3ac-f0137b393c98.serverhub.praktikum-services.ru'
CREATE_ORDER_PATH = '/api/v1/orders'
GET_ORDER_PATH = '/api/v1/orders/track'


order = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK"
    ]
}

headers = {
    "Content-Type": "application/json"
}


def create_order():
    return requests.post(BASE_URL + CREATE_ORDER_PATH, headers=headers, json=order)


def get_order(track):
    return requests.get(BASE_URL + GET_ORDER_PATH, headers=headers, params={"t": track})


def test_200():
    response = create_order()
    response = get_order(response.json()["track"])

    assert response.status_code == 200