import requests
import endpoints
import random
import time
import pytest


def generate_animal_payload():
    return {
        "name": f"test_animal{time.time()}",
        "kind": random.choice(["dog", "cat", "horse", "fish"]),
        "age": random.randint(1, 50)
    }


@pytest.fixture
def animal_id():
    payload = generate_animal_payload()
    create_response = requests.post(endpoints.animals_url, json=payload)
    assert create_response.status_code == 200
    animal_id = create_response.json()['id']
    return animal_id


class TestAnimals:

    def test_get_list_of_animals(self):
        get_list_response = requests.get(endpoints.animals_url)
        print(get_list_response.status_code)
        print(get_list_response.headers)
        print(get_list_response.text)
        print(get_list_response.json())
        print(len(get_list_response.json()))

        assert get_list_response.status_code == 200

    def test_create_new_animal(self, animal_id):

        details_response = requests.get(endpoints.animal_details_url(animal_id))
        assert details_response.status_code == 200

    def test_create_new_animal_with_invalid_json(self):
        payload = [generate_animal_payload()]
        create_response = requests.post(endpoints.animals_url, json=payload)
        assert create_response.status_code == 400

    def test_create_new_animal_with_missing_key(self):
        payload = generate_animal_payload()
        del payload['kind']
        create_response = requests.post(endpoints.animals_url, json=payload)
        assert create_response.status_code == 400

    def test_update_animal(self, animal_id):

        # Update animal with new data
        updated_payload = generate_animal_payload()
        put_animal = requests.put(endpoints.animal_details_url(animal_id), json=updated_payload)

        put_dict = put_animal.json()

        assert put_animal.status_code == 202
        assert put_dict['name'] == updated_payload['name']

        # Verify Animal details were updated
        get_updated_animal = requests.get(endpoints.animal_details_url(animal_id))
        get_updated_animal_dic = get_updated_animal.json()
        assert get_updated_animal_dic['name'] == updated_payload['name']

    def test_delete_animal(self, animal_id):
        # Delete animal
        delete_animal = requests.delete(endpoints.animal_details_url(animal_id))
        assert delete_animal.status_code == 204

        # Assert animal deleted
        get_deleted_animal = requests.get(endpoints.animal_details_url(animal_id))
        assert get_deleted_animal.status_code == 404
