import requests


class ApiService:
    def __init__(self, token=None):
        self.headers = {'x-api-key': 'reqres-free-v1', 'Content-Type': 'application/json'}
        if token:
            self.headers.update({'authorization': f'Bearer {token}'})
        self.base_url = 'https://reqres.in/api'

    def service_url(self, path):
        return self.base_url + path

    def get(self, path, headers=None, params=None, **kwargs):
        if headers:
            self.headers.update(headers)
        response = requests.get(self.service_url(path), params=params, headers=self.headers, **kwargs)
        return response

    def post(self, path, json, headers=None,  **kwargs):
        if headers:
            self.headers.update(headers)
        response = requests.get(self.service_url(path), json=json, headers=self.headers, **kwargs)
        return response
