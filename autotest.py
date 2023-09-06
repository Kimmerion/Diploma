# Максимова Александра Алексеевна, 8-я когорта — Финальный проект. Инженер по тестированию плюс
import requests


BASE_URL = 'https://2fb054ce-3b00-4f62-96e7-055b0af35da0.serverhub.praktikum-services.ru'
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