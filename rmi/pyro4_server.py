import Pyro4
import random

@Pyro4.expose
class OrderService:
    def __init__(self):
        # Tạo 1000 sản phẩm với giá random từ 100 - 10.000
        self.PRODUCTS = {f"P{i:04d}": random.randint(100, 10000) for i in range(1, 1001)}

    def calculate_total(self, product_code, quantity):
        if product_code not in self.PRODUCTS:
            return {"status": "FAILED", "total_price": 0.0, "message": "Product not found"}

        total_price = self.PRODUCTS[product_code] * quantity
        return {"status": "SUCCESS", "total_price": total_price, "message": "Order confirmed"}

# Khởi chạy Pyro4 Daemon
def main():
    daemon = Pyro4.Daemon()  # Tạo server Pyro4
    ns = Pyro4.locateNS()  # Kết nối đến Name Server
    uri = daemon.register(OrderService)  # Đăng ký class với Pyro4
    ns.register("order.service", uri)  # Đặt tên cho service
    print("OrderService is running...")
    daemon.requestLoop()  # Chạy vòng lặp nhận request

if __name__ == "__main__":
    main()
