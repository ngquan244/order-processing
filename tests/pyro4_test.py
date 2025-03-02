from locust import HttpUser, task, between


class LoadTestUser(HttpUser):
    wait_time = between(1, 3)  # thời gian chờ ngẫu nhiên giữa các requests từ 1 đến 3 giây

    @task
    def get_homepage(self):
        self.client.get("http://127.0.0.1:9090/")  # gửi yêu cầu GET đến trang chủ của server

    # @task
    # def get_about(self):
    #     self.client.get("http://127.0.0.1:5000/products")