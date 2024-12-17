from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/wiki/Locust")
        self.client.get("/wiki/Python")
