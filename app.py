from flask import Flask, request, jsonify
from db import create_tables, get_connection
from inventory import add_product

app = Flask(__name__)

create_tables()

API_KEY = "secret123"


def authenticate(req):
    return req.headers.get("x-api-key") == API_KEY


@app.route("/")
def home():
    return "Inventory API Running"


@app.route("/products", methods=["POST"])
def create_product():
    if not authenticate(request):
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json or {}

    name = data.get("name")
    price = data.get("price")
    quantity = data.get("quantity")

    if not name or not isinstance(price, (int, float)) or not isinstance(quantity, int):
        return jsonify({"error": "Invalid input"}), 400

    if price <= 0 or quantity <= 0:
        return jsonify({"error": "Price and quantity must be positive"}), 400

    try:
        add_product(name, price, quantity)
        return jsonify({"message": "Product added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/products", methods=["GET"])
def get_products():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, price, quantity FROM products")
    rows = cursor.fetchall()
    conn.close()

    products = [
        {"id": r[0], "name": r[1], "price": r[2], "quantity": r[3]}
        for r in rows
    ]

    return jsonify(products)


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
