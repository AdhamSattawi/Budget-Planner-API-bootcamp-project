# Budget Planner API 🚀

**Author:** Adham Sattawi
**Role:** Backend Developer

---

## 📖 About

The Budget Planner API is a robust backend service developed for managing personal finances. It was built with a strong emphasis on **Clean Architecture**, **Domain-Driven Design (DDD)**, and modern Python enterprise best practices.

This flagship project represents the capstone of my CodeValue Backend Development training, transitioning from fundamental Python techniques to a mature, scalable API architecture.

---

## 🛠️ Technology Stack

- **Framework:** FastAPI (Asynchronous API framework)
- **Database:** SQLAlchemy 2.0 (Async ORM)
- **Migrations:** Alembic
- **Testing:** Pytest & Pytest-Asyncio
- **Code Quality:** Flake8, Black, MyPy, and Wemake-python-styleguide (WPS)
- **Concurrency:** Asyncio for high-performance I/O operations

---

## 📂 Architecture

The project adopts a layered **Clean Architecture** pattern, ensuring clear separation of concerns, testability, and maintainability:

- **`api/` (Controllers):** FastAPI routers handling incoming HTTP requests, input validation, and HTTP responses.
- **`services/` (Use Cases):** Centralized business logic, transaction management, and coordination of domain entities.
- **`repository/` (Data Access):** Abstraction over the database using SQLAlchemy, isolating the ORM from business logic.
- **`models/` (Domain & ORM):** Data representations and strictly-typed database schemas.

---

## 🧪 Setup & Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/AdhamSattawi/backend-bootcamp-CodeValue.git
cd backend-bootcamp-CodeValue
```

### 2️⃣ Set up the virtual environment

#### Windows
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

#### Linux / Mac
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Project

For a better developer experience, use the provided `Makefile`.

*Note: For Windows without `make`, you can run the commands inside the Makefile directly.*

### Start the API Server
```bash
make run
# Or manually:
# cd budget_planner_api && uvicorn api.main:app --reload
```

### Run Tests
```bash
make test
# Or manually:
# pytest budget_planner_api/tests/
```

### Run Linters & Type Checking
```bash
make lint
# Or manually:
# flake8 budget_planner_api/
# mypy budget_planner_api/
```

---

## 🗃️ Bootcamp Archive

The historical exercises and assignments leading up to this capstone are preserved in the `bootcamp_archive` directory for reference. These reflect a clear progression of skill sets in core Python, object-oriented programming, concurrency, and web services.

---

This project was developed by Adham Sattawi as part of the professional backend track at **CodeValue**.
