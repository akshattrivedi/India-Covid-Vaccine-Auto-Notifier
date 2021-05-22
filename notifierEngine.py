import requests
from datetime import date

class NotifierEngine:
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
    timeInSecs = 5

    def __init__(self):
        pass


    def availability(self, centers: list, age: int, inputDate: str, vaccineType: str, dose: int) -> list: 
        availabilityList = []

        for center in centers:
            sessions = center["sessions"]
            
            for session in sessions:
                if (dose == 1 and session["available_capacity_dose1"] > 0) or (dose == 2 and session["available_capacity_dose2"] > 0) or (dose == 0 and session["available_capacity"] > 0):
                    """ dose = 0 -> all the doses (dose1 and dose2) """
                    if self.ageCategory(age) == session["min_age_limit"] or age == 0:
                        """ age = 0 -> all the ages are accepted """
                        if inputDate == session["date"] or inputDate == "0":
                            """ inputDate = 0 -> all the future upcoming dates """
                            if vaccineType == session["vaccine"] or vaccineType == "0":
                                """ vaccineType = 0 -> all the vaccines are accepted """
                                availabilityList.append(center)

        return availabilityList
                                     

    def fetchDataByDistrictID(self, districtID: int) -> dict:
        URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=" + str(districtID) + "&date=" + self.currentDate()
        response = requests.get(URL, headers = self.header)
        return response.json()["centers"]

    def fetchDataByPINCode(self, pincode: int) -> dict:
        URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=" + str(self.pincode) + "&date=" + self.currentDate()
        response = requests.get(URL, headers = self.header)
        return response.json()["centers"]

    def currentDate(self) -> str:
        """ Fetches the Today's Date in the Given Format """
        today = date.today()
        return today.strftime("%d-%m-%Y")

    def ageCategory(self, age: int) -> int:
        """ Age Category is decided by Minimum age Limit """
        if age >= 45: 
            return 45
        elif age >= 18 and age < 45:
            return 18
        elif age >= 3 and age < 18:
            return 3
        else:
            return -1



if __name__ == "__main__":
    districtID = 312
    pincode = 462003
    age = 50
    inputDate = "22-05-2021"
    vaccineType = "COVISHIELD"
    dose = 1

    notifierEngine = NotifierEngine()

    if districtID != -1:
        """ Fetching Data By District ID """
        centersList = notifierEngine.fetchDataByDistrictID(districtID)

    elif int(pincode/100000) != 0 and int(pincode/1000000) == 0:
        """ India's PIN Code is a 6 Digit Number """
        centersList = notifierEngine.fetchDataByPINCode(pincode)

    else:
        print("Input Error!")


    availability = notifierEngine.availability(centersList, age, inputDate, vaccineType, dose)
    print(availability)
    