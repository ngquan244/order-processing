from flask import Flask, request, jsonify
import random
import json

app = Flask(__name__)

# Tạo dtb 1000 sp với giá ngẫu nhiên từ 100 đến 10.000
PRODUCTS = {f"P{i:04d}": random.randint(100, 10000) for i in range(1, 1001)}

# 10 sp đầu tiên
for key, value in list(PRODUCTS.items())[:10]:
    print(f"{key}: {value}")


@app.route("/product/<product_code>", methods=["GET"])
def get_product(product_code):
    price = PRODUCTS.get(product_code)
    if price:
        return jsonify({"product_code": product_code, "price": price})
    return jsonify({"error": "Product not found"}), 404

@app.route("/products", methods=["GET"])
def get_all_products():
    json_data = json.dumps(PRODUCTS, indent=4)
    # JSON --> Text
    return app.response_class(json_data, content_type='text/plain')

@app.route("/order", methods=["POST"])
def create_order():
    data = request.json
    product_code = data["item"]
    quantity = data["quantity"]

    price = PRODUCTS.get(product_code)

    if price:
        total_price = price * quantity
        return jsonify({
            "message": "Order created!",
            "order": {
                "id": 123,
                "item": product_code,
                "quantity": quantity,
                "total_price": total_price
            }
        })
    return jsonify({"error": "Product not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
