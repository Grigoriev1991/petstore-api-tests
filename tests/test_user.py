from fixtures.user_fixtures import api_client, user


def test_create_user(user):
    new_user = {
        "id": 1,
        "username": "testuser",
        "firstName": "Test",
        "lastName": "User",
        "email": "testuser@example.com",
        "password": "password",
        "phone": "1234567890",
        "userStatus": 0
    }
    response = user.create_user(new_user)
    assert response.status_code == 200

def test_get_user_by_username(user):
    response = user.get_user_by_username("testuser")
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"

def test_update_user(user):
    updated_user = {
        "id": 1,
        "username": "testuser",
        "firstName": "Updated",
        "lastName": "User",
        "email": "updateduser@example.com",
        "password": "newpassword",
        "phone": "0987654321",
        "userStatus": 1
    }
    response = user.update_user("testuser", updated_user)
    assert response.status_code == 200

def test_delete_user(user):
    response = user.delete_user("testuser")
    assert response.status_code == 200

def test_login_user(user):
    response = user.login_user("testuser", "password")
    assert response.status_code == 200

def test_logout_user(user):
    response = user.logout_user()
    assert response.status_code == 200

def test_create_users_with_array(user):
    new_users = [
        {
            "id": 2,
            "username": "testuser2",
            "firstName": "Test2",
            "lastName": "User2",
            "email": "testuser2@example.com",
            "password": "password2",
            "phone": "1234567891",
            "userStatus": 0
        },
        {
            "id": 3,
            "username": "testuser3",
            "firstName": "Test3",
            "lastName": "User3",
            "email": "testuser3@example.com",
            "password": "password3",
            "phone": "1234567892",
            "userStatus": 0
        }
    ]
    response = user.create_users_with_array(new_users)
    assert response.status_code == 200

def test_create_users_with_list(user):
    new_users = [
        {
            "id": 4,
            "username": "testuser4",
            "firstName": "Test4",
            "lastName": "User4",
            "email": "testuser4@example.com",
            "password": "password4",
            "phone": "1234567893",
            "userStatus": 0
        },
        {
            "id": 5,
            "username": "testuser5",
            "firstName": "Test5",
            "lastName": "User5",
            "email": "testuser5@example.com",
            "password": "password5",
            "phone": "1234567894",
            "userStatus": 0
        }
    ]
    response = user.create_users_with_list(new_users)
    assert response.status_code == 200
