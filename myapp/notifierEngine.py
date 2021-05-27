"""
    Author: Akshat Trivedi
    Python Version: 3.9.2
"""

import requests
from datetime import date
import datetime

class NotifierEngine:
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

    def __init__(self):
        pass


    def availability(self, centers: list, age: int, inputDate: str, vaccineType: str, dose: int) -> list: 
        centersFilteredList = []
        inputDate = self.changeDateFormat(inputDate)

        for center in centers:
            sessions = center["sessions"]
            sessionsFilteredList = []
            sessionsCount = 0
            
            for session in sessions:
                if (dose == 1 and session["available_capacity_dose1"] > 0) or (dose == 2 and session["available_capacity_dose2"] > 0) or (dose == 0 and session["available_capacity"] > 0):
                    """ dose = 0 -> all the doses (dose1 and dose2) """
                    if self.ageGroup(age) == session["min_age_limit"] or age == 0:
                        """ age = 0 -> all the ages are accepted """
                        if inputDate == session["date"] or inputDate == "":
                            """ inputDate = "" -> all the future upcoming dates """
                            if vaccineType == session["vaccine"] or vaccineType == "":
                                """ vaccineType = "" -> all the vaccines are accepted """
                                session.pop("session_id","")
                                session.pop("slots","")

                                sessionsFilteredList.append(session)
                                sessionsCount = sessionsCount + 1

            if sessionsCount > 0:
                center.pop("center_id","")
                center.pop("lat","")
                center.pop("long","")
                center.pop("from","")
                center.pop("to","")

                center["sessions"] = sessionsFilteredList
                centersFilteredList.append(center)


        return centersFilteredList
                                     

    def fetchDataByDistrictID(self, districtID: int) -> dict:
        URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=" + str(districtID) + "&date=" + self.currentDate()
        response = requests.get(URL, headers = self.header)
        return response.json()["centers"]

    def fetchDataByPINCode(self, pincode: int) -> dict:
        URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=" + str(pincode) + "&date=" + self.currentDate()
        response = requests.get(URL, headers = self.header)
        return response.json()["centers"]

    def currentDate(self) -> str:
        """ Fetches the Today's Date in the Given Format """
        today = date.today()
        return today.strftime("%d-%m-%Y")

    def changeDateFormat(self, inputDate: str) -> str:
        if inputDate == "":
            return ""
        else:
            return datetime.datetime.strptime(inputDate, '%Y-%m-%d').strftime('%d-%m-%Y')

    def ageGroup(self, age: int) -> int:
        """ Age Group is decided by Minimum age Limit """
        if age >= 45: 
            return 45
        elif age >= 18 and age < 45:
            return 18
        elif age >= 3 and age < 18:
            return 3
        else:
            return -1



# if __name__ == "__main__":
#     districtID = 312
#     pincode = 462003
#     age = 50
#     inputDate = "24-05-2021"
#     vaccineType = "COVAXIN"
#     dose = 2

#     notifierEngine = NotifierEngine()

#     if districtID != -1:
#         """ Fetching Data By District ID """
#         centersList = notifierEngine.fetchDataByDistrictID(districtID)

#     elif int(pincode/100000) != 0 and int(pincode/1000000) == 0:
#         """ India's PIN Code is a 6 Digit Number """
#         centersList = notifierEngine.fetchDataByPINCode(pincode)

#     else:
#         print("Input Error!")


#     availability = notifierEngine.availability(centersList, age, inputDate, vaccineType, dose)
#     print(availability)
#     print(len(availability))
    