import requests
import unittest
from ya import Folders


class TestYapi(unittest.TestCase):
    def setUp(self):
        self.uploader = Folders("")

    def test_create_folder(self):
        test_directory = "rrrr"
        self.assertEqual(self.uploader.create_folder(test_directory).status_code, 201)
        response = requests.get("https://cloud-api.yandex.net/v1/disk/resources", 
                                params={"path": "/"},
                                headers={"Authorization": f"OAuth {self.uploader.token}"
        })

        fold = [f["name"] for f in response.json().get("_embedded").get("items") if f["type"] == "dir"]
        self.assertIn(test_directory, fold)

    def tearDown(self):
        print("тест завершен успешно")