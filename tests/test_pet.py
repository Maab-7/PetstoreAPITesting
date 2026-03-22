import allure
import pytest
from api.pet_api import PetAPI

PET_ID = 123456789

@pytest.fixture
def api():
    return PetAPI()


@allure.title("Obtener mascotas por status")
@allure.description("Verifica que se obtiene la lista de mascotas con status 'available'")
def test_get_pets_by_status(api):
    with allure.step("Hacer GET /pet/findByStatus?status=available"):
        response = api.get_pets_by_status(status="available")

    with allure.step("Verificar status code 200"):
        assert response.status_code == 200

    with allure.step("Verificar que la respuesta contiene mascotas"):
        data = response.json()
        assert len(data) > 0


@allure.title("Crear mascota")
@allure.description("Verifica que se puede crear una nueva mascota")
def test_create_pet(api):
    with allure.step("Hacer POST /pet"):
        response = api.create_pet(
            pet_id=PET_ID,
            name="Firulais",
            status="available"
        )

    with allure.step("Verificar status code 200"):
        assert response.status_code == 200

    with allure.step("Verificar datos de la mascota creada"):
        data = response.json()
        assert data["id"] == PET_ID
        assert data["name"] == "Firulais"
        assert data["status"] == "available"


@allure.title("Obtener mascota por ID")
@allure.description("Verifica que se obtiene una mascota específica por su ID")
def test_get_pet_by_id(api):
    with allure.step("Hacer GET /pet/{petId}"):
        response = api.get_pet_by_id(pet_id=PET_ID)

    with allure.step("Verificar status code 200"):
        assert response.status_code == 200

    with allure.step("Verificar datos de la mascota"):
        data = response.json()
        assert data["id"] == PET_ID
        assert data["name"] == "Firulais"


@allure.title("Actualizar mascota")
@allure.description("Verifica que se puede actualizar una mascota existente")
def test_update_pet(api):
    with allure.step("Hacer PUT /pet"):
        response = api.update_pet(
            pet_id=PET_ID,
            name="Firulais Updated",
            status="sold"
        )

    with allure.step("Verificar status code 200"):
        assert response.status_code == 200

    with allure.step("Verificar datos actualizados"):
        data = response.json()
        assert data["name"] == "Firulais Updated"
        assert data["status"] == "sold"


@allure.title("Obtener mascota inexistente")
@allure.description("Verifica que se retorna 404 para una mascota que no existe")
def test_get_pet_not_found(api):
    with allure.step("Hacer GET /pet/999999999"):
        response = api.get_pet_by_id(pet_id=999999999)

    with allure.step("Verificar status code 404"):
        assert response.status_code == 404


@allure.title("Eliminar mascota")
@allure.description("Verifica que se puede eliminar una mascota correctamente")
def test_delete_pet(api):
    with allure.step("Hacer DELETE /pet/{petId}"):
        response = api.delete_pet(pet_id=PET_ID)

    with allure.step("Verificar status code 200"):
        assert response.status_code == 200