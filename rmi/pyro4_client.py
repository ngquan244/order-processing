import Pyro4

order_service = Pyro4.Proxy("PYRONAME:order.service")

product_code = input("Nhập mã sản phẩm (VD: P0050): ").strip().upper()
quantity = input("Nhập số lượng: ").strip()

if not quantity.isdigit() or int(quantity) <= 0:
    print("Số lượng không hợp lệ!")
else:
    quantity = int(quantity)

    # Gửi yêu cầu đặt hàng
    response = order_service.calculate_total(product_code, quantity)

    # Hiển thị kết quả
    print(f"\nKết quả đơn hàng:")
    print(f"Trạng thái: {response['status']}")
    print(f"Tổng tiền: {response['total_price']}")
    print(f"Thông báo: {response['message']}")
