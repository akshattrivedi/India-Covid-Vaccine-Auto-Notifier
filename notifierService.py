from location import Location

class NotifierService:

    def __init__(self):
        pass

    def execute(self, stateName: str, districtName: str, pincode: int, age: int, inputDate: str, vaccineType: str, dose: int) -> list:
        location = Location()

        stateID     = location.getStateID(stateName)
        districtID  = location.getDistrictID(stateID, districtName)

        if districtID != -1:
            """ Fetching Data By District ID """
            centersList = notifierEngine.fetchDataByDistrictID(districtID)

        elif int(pincode/100000) != 0 and int(pincode/1000000) == 0:
            """ India's PIN Code is a 6 Digit Number """
            centersList = notifierEngine.fetchDataByPINCode(pincode)

        else:
            print("Input Error!")

        return notifierEngine.availability(centersList, age, inputDate, vaccineType, dose)
    

