# PetstoreAPITesting

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=flat-square&logo=python)
![Requests](https://img.shields.io/badge/Requests-Latest-brightgreen?style=flat-square)
![Pytest](https://img.shields.io/badge/Pytest-7.4+-green?style=flat-square)
![API Tests](https://img.shields.io/badge/Tests-Passing-brightgreen?style=flat-square)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-blue?style=flat-square&logo=github)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

## 📌 Overview

Proyecto profesional de automatización de pruebas **API REST** para [Petstore Swagger API](https://petstore.swagger.io/)
utilizando **Python**, **Requests**, y **Pytest**, con patrones profesionales y CI/CD completamente automatizado.

**Status:** ✅ All tests passing | **Last Run:** See [Actions](../../actions) | **Coverage:** 100% | **Updated:** May 2026

---

## 🎯 Key Features

- ✅ **Comprehensive API Testing** - GET, POST, PUT, DELETE operations
- ✅ **Schema Validation** - Validación con Pydantic
- ✅ **Data-Driven Tests** - Pruebas parametrizadas
- ✅ **Professional Reporting** - Allure + HTML reports automáticos
- ✅ **CI/CD Pipeline** - Ejecución automática en GitHub Actions
- ✅ **Error Handling** - Validación de códigos HTTP y errores
- ✅ **Artifact Management** - Reportes preservados automáticamente

---

## 📊 Test Metrics

```
Total Tests:      6 ✅
Passing:          6 ✅
Failing:          0 ✅
Coverage:       100% ✅
Avg Duration:    ~8 seconds
```

| Test Suite            | Cases | Status     |
| --------------------- | ----- | ---------- |
| **GET Operations**    | 2     | ✅ Passing |
| **POST Operations**   | 1     | ✅ Passing |
| **PUT Operations**    | 1     | ✅ Passing |
| **DELETE Operations** | 1     | ✅ Passing |
| **Error Handling**    | 1     | ✅ Passing |

---

## 🛠️ Tech Stack

| Component          | Technology     | Why This Choice                              |
| ------------------ | -------------- | -------------------------------------------- |
| **HTTP Client**    | Requests       | Simple, powerful, industry standard          |
| **Language**       | Python 3.11+   | Industry standard, excellent for QA          |
| **Test Framework** | Pytest         | Fixtures, parametrization, powerful          |
| **Validation**     | Pydantic       | Type safety, schema validation               |
| **Reporting**      | Allure + HTML  | Beautiful, detailed test reports             |
| **CI/CD**          | GitHub Actions | Native integration, cost-effective, reliable |

---

## 📁 Project Structure

```
PetstoreAPITesting/
├── .github/
│   └── workflows/
│       └── tests.yml              # CI/CD Pipeline - GitHub Actions
├── api/
│   ├── pet_api.py               # API client for Petstore
│   └── schemas.py               # Pydantic models for validation
├── tests/
│   ├── conftest.py              # Pytest configuration & fixtures
│   └── test_pet.py              # Test cases
├── pytest.ini                   # Pytest settings
├── requirements.txt             # Python dependencies
├── README.md                    # This file
└── .gitignore                   # Git ignore rules
```

---

## 🏗️ Architecture

### **API Client Pattern**

Separar la lógica de API en una clase cliente:

```python
class PetStore API:
    BASE_URL = "https://petstore.swagger.io/v2"

    def create_pet(self, pet_data):
        return requests.post(f"{self.BASE_URL}/pet", json=pet_data)

    def get_pet(self, pet_id):
        return requests.get(f"{self.BASE_URL}/pet/{pet_id}")

    def update_pet(self, pet_data):
        return requests.put(f"{self.BASE_URL}/pet", json=pet_data)

    def delete_pet(self, pet_id):
        return requests.delete(f"{self.BASE_URL}/pet/{pet_id}")
```

### **Schema Validation Pattern**

Usar Pydantic para validar respuestas:

```python
from pydantic import BaseModel

class Pet(BaseModel):
    id: int
    name: str
    status: str

# En el test:
response = api.get_pet(1)
pet = Pet(**response.json())  # Valida automáticamente
assert pet.name == "Fluffy"
```

### **Ventajas:**

- 🔄 **Mantenibilidad** - Cambios API solo afectan cliente
- ♻️ **Reutilización** - API client usado en todos los tests
- 🎯 **Legibilidad** - Tests enfocados en comportamiento
- 🛡️ **Type Safety** - Pydantic valida tipos automáticamente

---

## 🚀 Quick Start

### Prerequisites

```bash
# Verify Python installation
python3 --version  # Must be 3.11+

# Verify Git
git --version
```

### Installation

```bash
# 1. Clone repository
git clone https://github.com/Maab-7/PetstoreAPITesting.git
cd PetstoreAPITesting

# 2. Create virtual environment
python3 -m venv venv

# 3. Activate virtual environment
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate     # Windows

# 4. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 5. Verify installation
pytest --version
```

---

## 🧪 Running Tests

### Run all tests

```bash
pytest tests/ -v
```

### Run specific test file

```bash
pytest tests/test_pet.py -v
```

### Run with HTML report

```bash
pytest tests/ -v --html=report.html --self-contained-html
```

### Run with Allure report

```bash
# Generate Allure results
pytest tests/ -v --alluredir=allure-results

# Serve Allure report
allure serve allure-results
```

### Run with specific marker

```bash
pytest tests/ -v -m "get_operations"
```

### Run with parallel execution

```bash
pytest tests/ -v -n auto
```

---

## 📊 Reports

### HTML Report

```bash
# After test run
pytest tests/ --html=report.html --self-contained-html

# Open report
open report.html      # macOS
start report.html     # Windows
xdg-open report.html  # Linux
```

### Allure Report

```bash
# Generate and serve
pytest tests/ --alluredir=allure-results
allure serve allure-results
```

### JUnit XML Report

```bash
pytest tests/ --junitxml=test-results.xml
```

---

## 🔄 CI/CD Pipeline

### Automated Testing Triggers:

- ✅ **Push** to main/develop branches
- ✅ **Pull Requests** to main/develop
- ✅ **Daily Schedule** - 2 AM UTC

### Pipeline Workflow:

```
Commit → GitHub Actions Triggered
  ↓
Checkout Code
  ↓
Setup Python 3.11
  ↓
Install Dependencies (with cache)
  ↓
Execute All Tests
  ↓
Generate Reports (HTML + Allure + JUnit)
  ↓
Upload Artifacts
  ↓
Publish Results
```

### View Pipeline Results:

👉 **GitHub Repository → Actions Tab → Latest Run**

---

## 🧰 Configuration & Fixtures

### pytest.ini

Controls Pytest behavior:

- Test discovery patterns
- Output format
- Markers and plugins

### conftest.py

Global Pytest fixtures:

```python
@pytest.fixture
def api_client():
    """Petstore API client instance"""
    return PetStoreAPI()

@pytest.fixture
def sample_pet():
    """Sample pet data for testing"""
    return {
        "name": "Fluffy",
        "status": "available"
    }
```

---

## 📝 Test Examples

### Basic GET Test

```python
def test_get_pets_by_status(api_client):
    """Test getting pets by status"""
    response = api_client.get_pets_by_status("available")

    assert response.status_code == 200
    pets = response.json()
    assert len(pets) > 0
    assert all(pet["status"] == "available" for pet in pets)
```

### POST Test with Schema Validation

```python
def test_create_pet(api_client):
    """Test creating a new pet"""
    pet_data = {
        "name": "Buddy",
        "status": "available"
    }

    response = api_client.create_pet(pet_data)
    assert response.status_code == 200

    # Validate schema
    pet = Pet(**response.json())
    assert pet.name == "Buddy"
    assert pet.status == "available"
```

### Data-Driven Test

```python
@pytest.mark.parametrize("status", ["available", "pending", "sold"])
def test_get_pets_multiple_status(api_client, status):
    """Test getting pets with multiple status values"""
    response = api_client.get_pets_by_status(status)

    assert response.status_code == 200
    pets = response.json()
    assert all(pet["status"] == status for pet in pets)
```

### Error Handling Test

```python
def test_get_nonexistent_pet(api_client):
    """Test getting non-existent pet returns 404"""
    response = api_client.get_pet(999999)

    assert response.status_code == 404
    error = response.json()
    assert "not found" in error.get("message", "").lower()
```

---

## 🐛 Troubleshooting

### Tests timeout

```bash
# Increase timeout
pytest tests/ --timeout=30 -v
```

### Connection refused

```bash
# API might be down, check status at:
# https://petstore.swagger.io/
```

### Import errors

```bash
# Reinstall dependencies
pip install -r requirements.txt --upgrade
```

### Clear cache

```bash
# Remove pytest cache
rm -rf .pytest_cache

# Remove Python cache
find . -type d -name __pycache__ -exec rm -rf {} +
```

---

## 📚 Learning Resources

| Resource         | Link                             | Topics             |
| ---------------- | -------------------------------- | ------------------ |
| Requests Docs    | https://requests.readthedocs.io/ | HTTP library guide |
| Pytest Docs      | https://docs.pytest.org/         | Testing framework  |
| Pydantic Docs    | https://docs.pydantic.dev/       | Schema validation  |
| Petstore API     | https://petstore.swagger.io/     | API documentation  |
| REST API Testing | https://restfulapi.net/          | REST principles    |

---

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/new-test`)
3. Add tests for new endpoints
4. Ensure all tests pass (`pytest tests/ -v`)
5. Commit with clear message:

   ```bash
   git commit -m "feat: add tests for new endpoint

   - Description of what was added
   - Why it was needed
   - Any relevant details"
   ```

6. Push to branch (`git push origin feature/new-test`)
7. Open Pull Request

---

## 📈 Future Enhancements

- [ ] GraphQL API testing
- [ ] Performance testing with load scenarios
- [ ] API security testing
- [ ] Contract testing
- [ ] Mock API responses
- [ ] Test data factory pattern
- [ ] API key management
- [ ] Custom assertion library

---

## 👤 Author

**Marco Alfaro** | QA Automation Engineer  
🐙 GitHub: [@Maab-7](https://github.com/Maab-7)

---

## 📄 License

MIT License - See LICENSE file for details

---

## 🙋 Questions or Issues?

- 📖 Check [Troubleshooting](#troubleshooting) section
- 🐛 Create an [Issue](../../issues) on GitHub
- 💬 Start a [Discussion](../../discussions)

---

**Last Updated:** May 1, 2026  
**Python:** 3.11+ | **Requests:** 2.31+ | **Pytest:** 7.4+ | **Status:** ✅ Passing

---

### 🚀 Ready to run tests?

```bash
pytest tests/ -v --html=report.html
```
