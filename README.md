# Petstore API Testing

Proyecto de automatización de pruebas de API para [Petstore](https://petstore.swagger.io/) utilizando Python y Pytest.

## 🛠️ Tecnologías

- Python 3.x
- Requests
- Pytest
- Allure Reports
- Jenkins (CI/CD)

## 📁 Estructura del proyecto

```
PetstoreAPITesting/
├── api/
│   └── pet_api.py
├── tests/
│   └── test_pet.py
├── conftest.py
├── pytest.ini
└── requirements.txt
```

## ✅ Casos de prueba

| Test                      | Método | Endpoint            | Descripción                            |
| ------------------------- | ------ | ------------------- | -------------------------------------- |
| `test_get_pets_by_status` | GET    | `/pet/findByStatus` | Obtener mascotas por status            |
| `test_create_pet`         | POST   | `/pet`              | Crear una nueva mascota                |
| `test_get_pet_by_id`      | GET    | `/pet/{petId}`      | Obtener mascota por ID                 |
| `test_update_pet`         | PUT    | `/pet`              | Actualizar mascota existente           |
| `test_get_pet_not_found`  | GET    | `/pet/999999999`    | Verificar 404 para mascota inexistente |
| `test_delete_pet`         | DELETE | `/pet/{petId}`      | Eliminar mascota                       |

## 🚀 Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/Maab-7/PetstoreAPITesting.git
cd PetstoreAPITesting
```

### 2. Crear entorno virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar tests

```bash
pytest tests/test_pet.py -v
```

### 5. Ver reporte Allure

```bash
allure serve allure-results
```

## 📊 Allure Reports

El proyecto genera reportes detallados con Allure mostrando cada paso de los tests con duración y estado.

## 🔄 CI/CD

El proyecto está integrado con Jenkins para ejecución automática con generación de reportes Allure.

## 📖 Documentación API

La documentación completa de la API está disponible en [Petstore Swagger](https://petstore.swagger.io/).
