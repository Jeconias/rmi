import Pyro4
import json
import requests

@Pyro4.expose
class RMI:
    def search(self, cep : str) -> {}:

        BASE_API = "https://viacep.com.br/ws/{}/json/unicode/".format(cep)
        print(BASE_API)
        headers = {"content-type":"application/json"}

        response = requests.get(BASE_API)

        if response.status_code == 200:
            return {"status":True, "data":json.loads(response.content.decode("utf-8")), "message":"Request success"}
        else:
            return {"status":False, "data":None, "message":"Request Failed"}

daemon = Pyro4.Daemon(port=5000)
uri = daemon.register(RMI, "rmi")
print(uri)
daemon.requestLoop()