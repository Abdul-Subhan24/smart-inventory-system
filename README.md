# 🚀 Smart Inventory & Sales Management System

A **Python-based backend project** demonstrating real-world **Python Developer (0–2 years)** skills including REST APIs, database integration, authentication, and backend data analysis.

---

## 📌 Project Overview

The **Smart Inventory & Sales Management System** is a backend application built using **Python and Flask** to manage products and inventory data.

It follows clean coding practices, modular architecture, and RESTful design principles.  
The application uses **SQLite** for persistence and exposes **REST APIs** for CRUD operations.

This project is designed to reflect **industry-level expectations for entry-level Python / Backend developers**.

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
✔ API-key based authentication  
✔ Modular & scalable project structure  
✔ Backend data analysis & visualization  
✔ Error handling & input validation  

---

## 📂 Project Structure

```text
smart_inventory_system/
│
├── app.py                    # Flask app entry point
├── db.py                     # Database connection & table creation
├── inventory.py              # Inventory business logic
├── database.db               # SQLite database (auto-generated, ignored in git)
├── requirements.txt          # Project dependencies
├── README.md                 # Project documentation
│
├── models/                   # OOP-based data models
│   ├── __init__.py
│   ├── product.py
│   ├── user.py
│   └── order.py
│
├── analysis/                 # Offline data analysis
│   └── sales_analysis.py
│
├── tests/
│   └── test_cases.txt        # Manual test cases
│
├── .gitignore
└── venv/                     # Virtual environment (ignored)
```

---

## 🔗 API Design (RESTful Architecture)

The backend follows **REST (Representational State Transfer)** principles to ensure clean, scalable, and predictable APIs.

### 📘 Key REST Concepts

- Stateless communication  
- JSON-based request and response  
- Resource-based endpoints  
- Standard HTTP methods for CRUD operations  

### 🔄 HTTP Methods Used

| Method | Purpose | Endpoint |
|------|--------|----------|
| GET | Retrieve data | `/products` |
| POST | Create data | `/products` |
| PUT | Update data | `/products/<id>` |
| DELETE | Delete data | `/products/<id>` |

---

## 🔐 Authentication (API-Key Based)

Basic API-key authentication is implemented to protect sensitive endpoints.

### 📘 How It Works

- API key is passed in request headers  
- Unauthorized access returns `401 Unauthorized`  

### 🔑 Header Example

```text
x-api-key: secret123
```

### 🧪 Authentication Logic

```python
def authenticate(request):
    api_key = request.headers.get("x-api-key")
    return api_key == "secret123"
```

---

## 🔗 API Endpoints

### ➕ Add Product  
**POST /products**

```json
{
  "name": "Laptop",
  "price": 55000,
  "quantity": 10
}
```

---

### 📄 Get All Products  
**GET /products**

```json
[
  {
    "id": 1,
    "name": "Laptop",
    "price": 55000,
    "quantity": 10
  }
]
```

---

### ✏️ Update Product  
**PUT /products/<id>**

```json
{
  "name": "Laptop Pro",
  "price": 60000,
  "quantity": 8
}
```

---

### ❌ Delete Product  
**DELETE /products/<id>**

---

## 🗄️ Database Design (SQLite)

The application uses **SQLite**, a lightweight relational database suitable for learning and small backend applications.

### 📘 Database Characteristics

- Serverless and file-based  
- Supports relational design  
- Automatically initialized when the application starts  

### 📑 Tables

- `users`
- `products`
- `orders`

### 🧪 Table Creation Example

```python
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    quantity INTEGER NOT NULL
);
```

---

## 📊 Data Analysis & Visualization

The project includes an **offline analytics module** to demonstrate how backend data can be analyzed.

### 📘 Purpose

- Demonstrates backend data processing  
- Generates insights from inventory data  
- Visualizes results using charts  

### 🧪 Example (from `analysis/sales_analysis.py`)

```python
df = pd.read_sql_query(
    "SELECT name, price, quantity FROM products",
    conn
)

df["total_value"] = df["price"] * df["quantity"]
summary = df.groupby("name")["total_value"].sum()

summary.plot(kind="bar")
plt.show()
```

> Note: This analysis script is **not part of the Flask runtime** and is executed separately.

---

## ▶️ How the Application Runs

1. Flask app starts from `app.py`  
2. Database tables are initialized automatically  
3. API receives HTTP requests  
4. Business logic executes  
5. JSON responses are returned  

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Abdul-Subhan24/smart-inventory-system.git
cd smart-inventory-system
```

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
python app.py
```

Server runs at:

```text
http://127.0.0.1:5000
```

---

## 🧪 API Testing

### Tools Used

- Postman  
- Flask Development Server  

API requests can be tested using Postman by setting headers and request bodies.

---

## 🎯 Learning Outcomes

This project demonstrates:

- Python fundamentals & OOP  
- Flask backend development  
- REST API design  
- SQLite database interaction  
- Authentication basics  
- Backend data analysis & visualization  
- Debugging and real-world problem solving  

---

## 🔮 Future Enhancements

- JWT authentication  
- Role-based access control  
- Pagination & filtering  
- Cloud deployment (AWS / Render)  
- Frontend integration  

---

## 👨‍💻 Author

**Md Abdul Subhan**  
Python Developer | Data & ML Background  
📍 Hyderabad, India  

---
