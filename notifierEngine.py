import requests

class NotifierEngine():
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

    def __init__(self):
        pass

    def autoReferesher(self, timeInSecs):
        pass
    
    def getStatesList(self) -> list:
        URL = "https://cdn-api.co-vin.in/api/v2/admin/location/states"
        response = requests.get(URL, headers = self.header)
        return response.json()["states"]

    
    def getStatesNames(self) -> list:
        statesList = self.getStatesList()
        stateNames = []

        for state in statesList:
            stateNames.append(state["state_name"])

        return stateNames


    def getStateIDFromStateNames(self, stateName: str) -> int:
        statesList = self.getStatesList()
        
        for state in statesList:
            if state["state_name"] == stateName:
                return state["state_id"]

        return -1

     
notifierEngine = NotifierEngine()
print(notifierEngine.getStateIDFromStateNames("Madhya Pradesh"))

