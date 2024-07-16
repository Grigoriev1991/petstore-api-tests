from src.api_client import ApiClient


class User:

    def __init__(self, api_client: ApiClient):
        self.api_client = api_client

    def create_user(self, user_data):
        return self.api_client.post("/user", json=user_data)

    def get_user_by_username(self, username):
        return self.api_client.get(f"/user/{username}")

    def update_user(self, username, user_data):
        return self.api_client.put(f"/user/{username}", json=user_data)

    def delete_user(self, username):
        return self.api_client.delete(f"/user/{username}")

    def login_user(self, username, password):
        return self.api_client.get("/user/login", params={"username": username, "password": password})

    def logout_user(self):
        return self.api_client.get("/user/logout")

    def create_users_with_array(self, users_data):
        return self.api_client.post("/user/createWithArray", json=users_data)

    def create_users_with_list(self, users_data):
        return self.api_client.post("/user/createWithList", json=users_data)