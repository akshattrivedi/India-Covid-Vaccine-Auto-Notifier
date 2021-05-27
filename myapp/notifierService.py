"""
    Author: Akshat Trivedi
    Python Version: 3.9.2
"""

from myapp.location import Location
from myapp.config import configs
from myapp.notifierEngine import NotifierEngine

class NotifierService:

    def __init__(self):
        self.location = Location()

    
    def findSlots(self, stateName: str, districtName: str, pincode: int, age: int, inputDate: str, vaccineType: str, dose: int) -> list:
        notifierEngine = NotifierEngine()
        stateID     = self.location.getStateID(stateName)
        districtID  = self.location.getDistrictID(stateID, districtName)

        if districtID != -1:
            """ Fetching Data By District ID """
            centersList = notifierEngine.fetchDataByDistrictID(districtID)

        elif int(pincode/100000) != 0 and int(pincode/1000000) == 0:
            """ India's PIN Code is a 6 Digit Number """
            centersList = notifierEngine.fetchDataByPINCode(pincode)

        else:
            return ["Input Error!"]

        return notifierEngine.availability(centersList, age, inputDate, vaccineType, dose)
    

    def getAllStates(self) -> list:
        return self.location.getStatesNames()

    
    def getAllDistricts(self, stateName :str) -> list:
        stateID = self.location.getStateID(stateName)
        return self.location.getDistrictsNames(stateID)


    def getAllVaccines(self) -> list:
        return configs.data["vaccineTypes"]

    def getAllDoses(self) -> list:
        return configs.data["doses"]

    def getAllAges(self) -> list:
        return configs.data["ages"]