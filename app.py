from flask import Flask, request, jsonify
from db import create_tables, get_connection

app = Flask(__name__)

# Initialize database tables
create_tables()

@app.route("/")
def home():
    return "Inventory API Running"

# -----------------------------
# Basic Authentication
# -----------------------------
def authenticate(request):
    api_key = request.headers.get("x-api-key")
    return api_key == "secret123"

# -----------------------------
# Product APIs
# -----------------------------
@app.route("/products", methods=["POST"])
def add_product():
    if not authenticate(request):
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json
    name = data.get("name")
    price = data.get("price")
    quantity = data.get("quantity")

    if not name or price is None or quantity is None:
        return jsonify({"error": "Invalid input"}), 400

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)",
        (name, price, quantity)
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Product added successfully"}), 201


@app.route("/products", methods=["GET"])
def get_products():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()

    conn.close()

    products = []
    for row in rows:
        products.append({
            "id": row[0],
            "name": row[1],
            "price": row[2],
            "quantity": row[3]
        })

    return jsonify(products)


@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    if not authenticate(request):
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE products SET name=?, price=?, quantity=? WHERE id=?",
        (data["name"], data["price"], data["quantity"], product_id)
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Product updated"})


@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    if not authenticate(request):
        return jsonify({"error": "Unauthorized"}), 401

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM products WHERE id=?", (product_id,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Product deleted"})


if __name__ == "__main__":
    app.run(debug=True)
