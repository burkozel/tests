import requests


class Folders:
    #TOKEN = ""
    #HEADERS = {"Authorization": f"OAuth{TOKEN}"}

    def __init__(self, token):
        self.token = token

    def create_folder(self, folder):
        HEADERS = {"Authorization": f'OAuth {self.token}'}
        URL = "https://cloud-api.yandex.net/v1/disk/resources"

        response = requests.put(URL, params={"path": "/" + folder}, headers=HEADERS)
        return response