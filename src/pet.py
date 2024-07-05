from src.api_client import ApiClient


class Pet:
    def __init__(self, api_client: ApiClient):
        self.api_client = api_client

    def get_pet_by_id(self, pet_id):
        return self.api_client.get(f"/pet/{pet_id}")

    def add_pet(self, pet_data):
        return self.api_client.post("/pet", json=pet_data)

    def update_pet(self, pet_data):
        return self.api_client.put("/pet", json=pet_data)

    def delete_pet(self, pet_id):
        return self.api_client.delete(f"/pet/{pet_id}")

    def find_pets_by_status(self, status):
        return self.api_client.get("/pet/findByStatus", params={"status": status})

    def find_pets_by_tags(self, tags):
        return self.api_client.get("/pet/findByTags", params={"tags": tags})

    def update_pet_with_form(self, pet_id, name=None, status=None):
        data = {}
        if name:
            data["name"] = name
        if status:
            data["status"] = status
        return self.api_client.post(f"/pet/{pet_id}", data=data)

    def upload_image(self, pet_id, file, additional_metadata=None):
        files = {"file": file}
        data = {}
        if additional_metadata:
            data["additionalMetadata"] = additional_metadata
        return self.api_client.post(f"/pet/{pet_id}/uploadImage", files=files, data=data)