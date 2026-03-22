import requests

BASE_URL = "https://petstore.swagger.io/v2"
API_KEY = "special-key"

HEADERS = {
    "Content-Type": "application/json",
    "api_key": API_KEY
}

class PetAPI:

    def get_pets_by_status(self, status):
        return requests.get(
            f"{BASE_URL}/pet/findByStatus",
            params={"status": status},
            headers=HEADERS
        )

    def get_pet_by_id(self, pet_id):
        return requests.get(
            f"{BASE_URL}/pet/{pet_id}",
            headers=HEADERS
        )

    def create_pet(self, pet_id, name, status):
        payload = {
            "id": pet_id,
            "name": name,
            "status": status
        }
        return requests.post(
            f"{BASE_URL}/pet",
            json=payload,
            headers=HEADERS
        )

    def update_pet(self, pet_id, name, status):
        payload = {
            "id": pet_id,
            "name": name,
            "status": status
        }
        return requests.put(
            f"{BASE_URL}/pet",
            json=payload,
            headers=HEADERS
        )

    def delete_pet(self, pet_id):
        return requests.delete(
            f"{BASE_URL}/pet/{pet_id}",
            headers=HEADERS
        )