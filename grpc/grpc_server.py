import grpc
from concurrent import futures
import order_pb2
import order_pb2_grpc
import random

# Tạo dtb 1000 sản phẩm với giá random
PRODUCTS = {f"P{i:04d}": random.randint(100, 10000) for i in range(1, 1001)}


class OrderServiceServicer(order_pb2_grpc.OrderServiceServicer):

    # Implement CreateOrder
    def CreateOrder(self, request, context):
        product_code = request.product_code
        quantity = request.quantity
        print(f"Received request: Product code: {product_code}, Quantity: {quantity}")

        if product_code not in PRODUCTS:
            context.set_details(f"Product {product_code} not found")
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return order_pb2.CreateOrderResponse()

        price_per_item = PRODUCTS[product_code]
        total_price = price_per_item * quantity

        # phản hồi th tin đơn hàng
        return order_pb2.CreateOrderResponse(
            message="Order created!",
            order_id=random.randint(100, 999),  # Giả lập ID đơn hàng
            product_code=product_code,
            quantity=quantity,
            total_price=total_price
        )


# Chạy server gRPC
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    order_pb2_grpc.add_OrderServiceServicer_to_server(OrderServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    print("Server is running on port 50051...")
    server.start()
    server.wait_for_termination()
def GetOrder(self, request, context):
    order_id = request.order_id
    # Giả sử bạn có cơ sở dữ liệu hoặc danh sách đơn hàng
    # Ở đây, ta chỉ dùng ví dụ giả lập
    if order_id == 272:  # Giả lập đơn hàng
        return order_pb2.CreateOrderResponse(
            message="Order found!",
            order_id=order_id,
            product_code="P0001",
            quantity=10,
            total_price=1000.0
        )
    context.set_details("Order not found!")
    context.set_code(grpc.StatusCode.NOT_FOUND)
    return order_pb2.CreateOrderResponse()

def UpdateOrder(self, request, context):
    order_id = request.order_id
    new_quantity = request.quantity
    product_code = request.product_code
    # Cập nhật đơn hàng ở đây
    return order_pb2.CreateOrderResponse(
        message="Order updated!",
        order_id=order_id,
        product_code=product_code,
        quantity=new_quantity,
        total_price=PRODUCTS[product_code] * new_quantity
    )
def DeleteOrder(self, request, context):
    order_id = request.order_id
    # Giả sử ta xóa đơn hàng ở đây
    return order_pb2.CreateOrderResponse(
        message="Order deleted!",
        order_id=order_id,
        product_code="P0001",
        quantity=0,
        total_price=0.0
    )


if __name__ == '__main__':
    serve()
