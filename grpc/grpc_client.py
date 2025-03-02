import grpc
import order_pb2
import order_pb2_grpc

# Gửi yêu cầu đến server
def create_order(product_code, quantity):
    # Connect với server gRPC
    channel = grpc.insecure_channel('localhost:50051')
    stub = order_pb2_grpc.OrderServiceStub(channel)

    # CreateOrderRequest
    order_request = order_pb2.CreateOrderRequest(
        product_code=product_code,
        quantity=quantity
    )

    response = stub.CreateOrder(order_request)
    return response

# Main
if __name__ == "__main__":
    # Nhập mã sản phẩm và số lượng từ người dùng
    product_code = input("Nhập mã sản phẩm (ví dụ: P0001): ")
    quantity = int(input("Nhập số lượng: "))

    # Gửi y cầu
    order = create_order(product_code, quantity)

    # Print Result
    print("Đơn hàng đã được tạo:")
    print(f"Message: {order.message}")
    print(f"Order ID: {order.order_id}")
    print(f"Product Code: {order.product_code}")
    print(f"Quantity: {order.quantity}")
    print(f"Total Price: {order.total_price}")
