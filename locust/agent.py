import sys
from locust import HttpUser, between, task
image_path = ''
HOST = ''
class APIPost(HttpUser):
    host = HOST
    wait_time = between(3,5)

    @task()
    def predict_dat(self):
        files = {'file':open(image_path,'rb')}
        self.client.post('/',files=files)