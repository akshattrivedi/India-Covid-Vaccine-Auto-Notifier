"""
    Author: Akshat Trivedi
    Python Version: 3.9.2
"""

from django.shortcuts import render
from myapp.notifierService import NotifierService
from rest_framework.decorators import api_view
from rest_framework.response import Response


notifierService = NotifierService()

def index(request):

    states = notifierService.getAllStates()
    ages = notifierService.getAllAges()
    vaccines = notifierService.getAllVaccines()
    doses = notifierService.getAllDoses()

    if request.method == "POST":
        stateName = request.POST.get("state", "")
        districts = notifierService.getAllDistricts(stateName)
        districtName = request.POST.get("district", "")
        pincode = request.POST.get("pincode", 0)
        age = request.POST.get("age", 0)
        inputDate = request.POST.get("date", "")
        vaccineType = request.POST.get("vaccineType", "")
        dose = request.POST.get("dose", 0)

        if pincode == "":
            pincode = 0
        else:
            pincode = int(pincode)
        if age == "":
            age = 0
        else:
            age = int(age)
        if dose == "":
            dose = 0
        else:
            dose = int(dose)

        slots = notifierService.findSlots(stateName, districtName, pincode, age, inputDate, vaccineType, dose)

        context = { "states": states, "districts": districts, "ages": ages, "vaccines": vaccines, "doses": doses, "stateSelected": stateName, "districtSelected": districtName,
        "pincodeEntered": pincode, "ageSelected": age, "dateSelected": inputDate, "vaccineTypeSelected": vaccineType, "doseSelected": dose, "slots" : slots}
        return render(request,'myapp/index.html', context)
    else:
        context = { "states": states, "ages": ages, "vaccines": vaccines, "doses": doses}
        return render(request,'myapp/index.html', context)


@api_view(['GET'])
def getAllDistricts(request):
    if request.method == "GET":
        stateName = request.query_params["state"]
        districts = notifierService.getAllDistricts(stateName)
        context = { "districts" : districts }
        return Response(context)


@api_view(['GET'])
def getSlots(request):
    if request.method == "GET":
        stateName = request.GET.get("state", "")
        districtName = request.GET.get("district", "")
        pincode = request.GET.get("pincode", 0)
        age = request.GET.get("age", 0)
        inputDate = request.GET.get("date", "")
        vaccineType = request.GET.get("vaccineType", "")
        dose = request.GET.get("dose", 0)
        

        if pincode == "":
            pincode = 0
        else:
            pincode = int(pincode)
        if age == "":
            age = 0
        else:
            age = int(age)
        if dose == "":
            dose = 0
        else:
            dose = int(dose)

        slots = notifierService.findSlots(stateName, districtName, pincode, age, inputDate, vaccineType, dose)
        context = {"slots": slots}
        return Response(context)
