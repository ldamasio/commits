import requests
import json
from decouple import config 

TOKEN = config('TOKEN')

class CommitsList():

    def __init__(self, usuario):
        self._usuario = usuario

    def api_request(self):
        response = requests.get(
            f'https://api.github.com/search/commits?q=author:ldamasio&order=desc&')
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code

    def printRepo(self):
        api_data = self.api_request()
        if type(api_data) is not int:
            for i in range(len(api_data)):
                print(json.dumps(api_data, indent=4))
        else:
            print(api_data)

repositorios = CommitsList('ldamasio')
repositorios.printRepo()
