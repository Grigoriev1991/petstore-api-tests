import tempfile

from fixtures.pet_fixtures import api_client, pet


def test_get_pet_by_id(pet):
    response = pet.get_pet_by_id(1)
    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_add_pet(pet):
    new_pet = {
        "id": 12345,
        "name": "TestPet",
        "photoUrls": [],
        "tags": [],
        "status": "available"
    }
    response = pet.add_pet(new_pet)
    assert response.status_code == 200
    assert response.json()["name"] == "TestPet"


def test_update_pet(pet):
    updated_pet = {
        "id": 12345,
        "name": "UpdatedTestPet",
        "photoUrls": [],
        "tags": [],
        "status": "available"
    }
    response = pet.update_pet(updated_pet)
    assert response.status_code == 200
    assert response.json()["name"] == "UpdatedTestPet"


def test_delete_pet(pet):
    response = pet.delete_pet(12345)
    assert response.status_code == 200
    assert response.json()["message"] == "12345"


def test_find_pets_by_status(pet):
    response = pet.find_pets_by_status("available")
    assert response.status_code == 200
    pets = response.json()
    assert isinstance(pets, list)
    assert len(pets) > 0

def test_find_pets_by_tags(pet):
    response = pet.find_pets_by_tags(["tag1", "tag2"])
    assert response.status_code == 200
    pets = response.json()
    assert isinstance(pets, list)

def test_update_pet_with_form(pet):
    response = pet.update_pet_with_form(1, name="UpdatedName", status="sold")
    assert response.status_code == 200

def test_upload_image(pet):
    with tempfile.NamedTemporaryFile(suffix=".jpg") as tmp_file:
        tmp_file.write(b"Fake image content")
        tmp_file.seek(0)
        response = pet.upload_image(1, tmp_file, "additional data")
    assert response.status_code == 200
