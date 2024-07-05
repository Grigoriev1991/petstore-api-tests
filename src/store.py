from src.api_client import ApiClient


class Store:
    def __init__(self, api_client: ApiClient):
        self.api_client = api_client

    def get_inventory(self):
        return self.api_client.get("/store/inventory")

    def place_order(self, order_data):
        return self.api_client.post("/store/order", json=order_data)

    def get_order_by_id(self, order_id):
        return self.api_client.get(f"/store/order/{order_id}")

    def delete_order(self, order_id):
        return self.api_client.delete(f"/store/order/{order_id}")
