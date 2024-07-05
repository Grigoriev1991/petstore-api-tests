from fixtures.store_fixtures import api_client, store


def test_get_inventory(store):
    response = store.get_inventory()
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_place_order(store):
    new_order = {
        "id": 1,
        "petId": 1,
        "quantity": 1,
        "shipDate": "2024-07-05T12:34:56.789Z",
        "status": "placed",
        "complete": True
    }
    response = store.place_order(new_order)
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_get_order_by_id(store):
    response = store.get_order_by_id(1)
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_delete_order(store):
    response = store.delete_order(1)
    assert response.status_code == 200
    assert response.json()["message"] == "1"
