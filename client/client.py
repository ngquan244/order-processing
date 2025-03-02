import requests

SERVER_URL = "http://127.0.0.1:5000"


def get_product_price(product_code):
    response = requests.get(f"{SERVER_URL}/product/{product_code}")
    if response.status_code == 200:
        return response.json().get("price")
    else:
        print("Không tìm thấy sản phẩm!")
        return None


def create_order(product_code, quantity):
    price = get_product_price(product_code)
    if price is None:
        return None

    total_price = price * quantity
    data = {"item": product_code, "quantity": quantity, "total_price": total_price}
    response = requests.post(f"{SERVER_URL}/order", json=data)

    return response.json()


if __name__ == "__main__":
    product_code = input("Nhập mã sản phẩm (ví dụ: P0001): ").strip()
    quantity = int(input("Nhập số lượng: ").strip())

    order = create_order(product_code, quantity)

    if order:
        print(f"Đơn hàng đã tạo: {order}")
    else:
        print("Đặt hàng thất bại!")
