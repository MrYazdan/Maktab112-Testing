# pip install locust
from locust import HttpUser, TaskSet, task, between


class HomeResponseTask(TaskSet):
    @task
    def get_response(self):
        self.client.get('http://127.0.0.1:8091')


class MaktabUser(HttpUser):
    tasks = [HomeResponseTask]
    wait_time = between(1, 3)
