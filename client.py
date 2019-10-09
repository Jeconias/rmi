import Pyro4

class RMIClient:
    def __init__(self, nameserver: str):
        self.pyroIdentify = nameserver


    def search(self, search : str):
        if search == "" or (not search.isnumeric()):
            print("Por favor digite um CEP válido.")
            return
        o = Pyro4.Proxy(self.pyroIdentify)
        r = o.search(search)
        if r["status"] == True:
            self.formatReturn(r["data"])
        else:
            print(r["message"])

    def formatReturn(self, response : str):
        print("\nCEP: {}\nCIDADE: {}\nBAIRRO: {}\nESTADO: {}".format(response["cep"], response["localidade"], response["bairro"], response["uf"]))


RMIClient = RMIClient("PYRO:rmi@localhost:5000")
cep = input("Digite um CEP para pesquisar: ")
RMIClient.search(cep)

