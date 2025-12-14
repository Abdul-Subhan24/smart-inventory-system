# 🚀 Smart Inventory & Sales Management System

A **Python-based backend project** demonstrating real-world **Python Developer (0–2 years)** skills including REST APIs, database integration, authentication, and data analysis.

---

## 📌 Project Overview

The **Smart Inventory & Sales Management System** is a backend application built using **Python and Flask** to manage products, inventory, and sales data.  
It follows clean coding practices, modular architecture, and RESTful design principles.

This project is designed to reflect **industry-level expectations for entry-level Python developers**.

---

## 🛠️ Tech Stack

- **Language:** Python 3  
- **Framework:** Flask  
- **Database:** SQLite  
- **Data Analysis:** Pandas, NumPy  
- **Visualization:** Matplotlib  
- **Tools:** Git, GitHub, Postman, VS Code  
- **Environment:** Python Virtual Environment (venv)

---

## ✨ Key Features

✔ RESTful API architecture  
✔ CRUD operations (Create, Read, Update, Delete)  
✔ SQLite database integration  
✔ JSON-based request & response handling  
✔ Basic API-key authentication  
✔ Modular & scalable project structure  
✔ Sales data analysis and visualization  
✔ Error handling & input validation  

---

## 📂 Project Structure

```text
smart_inventory_system/
│
├── app.py                # Flask app entry point
├── db.py                 # Database connection & table creation
├── database.db           # SQLite database (auto-generated)
├── requirements.txt      # Project dependencies
├── README.md             # Documentation
│
├── models/               # OOP-based data models
│   ├── __init__.py
│   ├── product.py
│   ├── user.py
│   └── order.py
│
├── data/                 # CSV files for analytics
│   ├── inventory.csv
│   └── sales.csv
│
├── analysis.py           # Data analysis & visualization
└── venv/                 # Virtual environment

## 🔗 API Design (RESTful Architecture)

The backend follows **REST (Representational State Transfer)** principles to ensure clean, scalable, and predictable APIs.

### 📘 Theory

- REST APIs are stateless  
- Communication happens using JSON  
- Each endpoint represents a resource  
- Standard HTTP methods are used for CRUD operations  

### 🔄 HTTP Methods Used

| Method | Purpose | Example |
|------|--------|---------|
| GET | Retrieve data | `/products` |
| POST | Create data | `/products` |
| PUT | Update data | `/products/<id>` |
| DELETE | Delete data | `/products/<id>` |

### 🧪 Example Endpoint

```python
@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)

### 🔐 Authentication (API-Key Based)

Basic API-key authentication is implemented to protect sensitive endpoints.

### 📘 Theory

- Authentication ensures only authorized access
- API key is passed in request headers
- Unauthorized access returns 401 Unauthorized

### 🔑 Header Example

x-api-key: secret123

### 🧪 Authentication Logic

def authenticate(request):
    api_key = request.headers.get("x-api-key")
    return api_key == "secret123"

### 🔗 API Endpoints
## ➕ Add Product

## POST /products
{
  "name": "Laptop",
  "price": 55000,
  "quantity": 10
}

### 📄 Get All Products

## GET /products

[
  {
    "id": 1,
    "name": "Laptop",
    "price": 55000,
    "quantity": 10
  }
]

### ✏️ Update Product

## PUT /products/<id>
{
  "name": "Laptop Pro",
  "price": 60000,
  "quantity": 8
}

### ❌ Delete Product

### DELETE /products/<id>

### 🗄️ Database Design (SQLite)
The application uses SQLite, a lightweight relational database.

### 📘 Theory

- SQLite is serverless and easy to use
- Ideal for learning and small applications
- Supports relational database concepts

### 📑 Tables

- users
- products
- orders

### 🧪 Table Creation Example

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    quantity INTEGER NOT NULL
)
""")

Tables are created automatically when the application starts.

### 📊 Data Analysis & Visualization
The project includes analytics to demonstrate backend data handling.

### 📘 Theory

- Backend systems often generate reports and insights
- Pandas handles data manipulation
- Matplotlib handles visualization

### 🧪 Example
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/sales.csv")
summary = df.groupby("product")["amount"].sum()

summary.plot(kind="bar")
plt.show()

### ▶️ How the Application Runs
## 📘 Theory

1. Flask app starts from app.py
2. Database tables are initialized
3. API receives request
4. Business logic executes
5. JSON response is returned

### ▶️ How to Run the Project
## 1️⃣ Clone the Repository

git clone https://github.com/Abdul-Subhan24/smart-inventory-system.git
cd smart-inventory-system

## 2️⃣ Create & Activate Virtual Environment

python -m venv venv
venv\Scripts\activate

## 3️⃣ Install Dependencies

pip install -r requirements.txt

## 4️⃣ Run the Application

python app.py

## Server runs at:

http://127.0.0.1:5000

### 🧪 API Testing
### 📘 Theory

- API testing validates correctness
- Postman simulates client requests

### 🛠️ Tools Used

- Postman
- Flask Development Server

### 🎯 Learning Outcomes
### 📘 Theory

This project demonstrates:

 - Python fundamentals & OOP
 - Flask backend development
 - REST API design
 - SQLite database interaction
 - Authentication basics
 - Data analysis & visualization
 - Debugging and real-world problem solving

### 🔮 Future Enhancements
### 📘 Theory

- JWT authentication
- Role-based access control
- Pagination & filtering
- Cloud deployment (AWS / Render)
- Frontend integration

### 👨‍💻 Author

## Md Abdul Subhan
Python Developer | Data & ML Background
📍 Hyderabad, India





