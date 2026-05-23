import allure
import pytest
from api.pet_api import PetAPI

# IDs únicos para cada test
PET_ID_CREATE = 123456789
PET_ID_NOT_FOUND = 999999999


@pytest.fixture
def api():
    return PetAPI()


@pytest.fixture
def pet_for_operations(api):
    """
    Fixture que crea un pet, lo usa en tests, y lo elimina después.
    Esto asegura limpieza automática.
    """
    # SETUP: Crear pet
    create_response = api.create_pet(
        pet_id=PET_ID_CREATE,
        name="Firulais",
        status="available"
    )
    assert create_response.status_code == 200, "Setup failed: couldn't create pet"
    
    yield  # Tests que usan esta fixture corren aquí
    
    # TEARDOWN: Eliminar pet (cleanup)
    api.delete_pet(pet_id=PET_ID_CREATE)


# ============ TEST 1 ============
@allure.title("Obtener mascotas por status")
@allure.description("Verifica que se obtiene la lista de mascotas con status 'available'")
def test_get_pets_by_status(api):
    """NO necesita pet específico - usa endpoint general"""
    with allure.step("Hacer GET /pet/findByStatus?status=available"):
        response = api.get_pets_by_status(status="available")

    with allure.step("Verificar status code 200"):
        assert response.status_code == 200

    with allure.step("Verificar que la respuesta contiene mascotas"):
        data = response.json()
        assert len(data) > 0


# ============ TEST 2 ============
@allure.title("Crear mascota")
@allure.description("Verifica que se puede crear una nueva mascota")
def test_create_pet(api):
    """Crea mascota y luego cleanup automático"""
    with allure.step("Hacer POST /pet"):
        response = api.create_pet(
            pet_id=PET_ID_CREATE,
            name="Firulais",
            status="available"
        )

    with allure.step("Verificar status code 200"):
        assert response.status_code == 200

    with allure.step("Verificar datos de la mascota creada"):
        data = response.json()
        assert data["id"] == PET_ID_CREATE
        assert data["name"] == "Firulais"
        assert data["status"] == "available"
    
    # CLEANUP: Eliminar el pet que creamos
    api.delete_pet(pet_id=PET_ID_CREATE)


# ============ TEST 3 ============
@allure.title("Obtener mascota por ID")
@allure.description("Verifica que se obtiene una mascota específica por su ID")
def test_get_pet_by_id(api, pet_for_operations):
    """Usa fixture que crea/limpia pet automáticamente"""
    with allure.step("Hacer GET /pet/{petId}"):
        response = api.get_pet_by_id(pet_id=PET_ID_CREATE)

    with allure.step("Verificar status code 200"):
        assert response.status_code == 200

    with allure.step("Verificar datos de la mascota"):
        data = response.json()
        assert data["id"] == PET_ID_CREATE
        assert data["name"] == "Firulais"


# ============ TEST 4 ============
@allure.title("Actualizar mascota")
@allure.description("Verifica que se puede actualizar una mascota existente")
def test_update_pet(api, pet_for_operations):
    """Usa fixture que crea/limpia pet automáticamente"""
    with allure.step("Hacer PUT /pet"):
        response = api.update_pet(
            pet_id=PET_ID_CREATE,
            name="Firulais Updated",
            status="sold"
        )

    with allure.step("Verificar status code 200"):
        assert response.status_code == 200

    with allure.step("Verificar datos actualizados"):
        data = response.json()
        assert data["name"] == "Firulais Updated"
        assert data["status"] == "sold"


# ============ TEST 5 - EL CRÍTICO ============
@allure.title("Obtener mascota inexistente")
@allure.description("Verifica que se retorna 404 para una mascota que no existe")
def test_get_pet_not_found(api):
    """
    TEST INDEPENDIENTE - No depende de otros tests.
    Usa ID que NUNCA será creado por otros tests.
    """
    with allure.step(f"Hacer GET /pet/{PET_ID_NOT_FOUND}"):
        response = api.get_pet_by_id(pet_id=PET_ID_NOT_FOUND)

    with allure.step("Verificar status code 404"):
        # Si el API devuelve 200 para pets inexistentes,
        # descomenta la línea siguiente en lugar de assert 404
        assert response.status_code == 404
        
        # ALTERNATIVA si el API NO devuelve 404:
        # data = response.json()
        # assert data == {} or data is None  # Validar que está vacío


# ============ TEST 6 ============
@allure.title("Eliminar mascota")
@allure.description("Verifica que se puede eliminar una mascota correctamente")
def test_delete_pet(api):
    """Crea mascota, la elimina, verifica eliminación"""
    # SETUP: Crear el pet primero
    create_response = api.create_pet(
        pet_id=PET_ID_CREATE,
        name="Firulais",
        status="available"
    )
    assert create_response.status_code == 200
    
    # ACT: Eliminar el pet
    with allure.step("Hacer DELETE /pet/{petId}"):
        response = api.delete_pet(pet_id=PET_ID_CREATE)

    # ASSERT: Verificar eliminación exitosa
    with allure.step("Verificar status code 200"):
        assert response.status_code == 200
    
    # VERIFY: Confirmar que realmente fue eliminado
    with allure.step("Verificar que el pet fue eliminado"):
        verify_response = api.get_pet_by_id(pet_id=PET_ID_CREATE)
        # Debería retornar 404 o error
        assert verify_response.status_code in [404, 500]