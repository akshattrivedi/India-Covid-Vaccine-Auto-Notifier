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

    # if request.GET.get('state'):
    if request.method == "POST":
        print(request.POST)
        return render(request,'myapp/index.html')
    else:
        states = notifierService.getAllStates()
        ages = notifierService.getAllAges()
        vaccines = notifierService.getAllVaccines()
        doses = notifierService.getAllDoses()
        context = { "states": states, "ages": ages, "vaccines": vaccines, "doses": doses}
        return render(request,'myapp/index.html',context)


@api_view(['GET'])
def getAllDistricts(request):
    if request.method == "GET":
        stateName = request.query_params["state"]
        districts = notifierService.getAllDistricts(stateName)
        context = { "districts" : districts }
        return Response(context)

    
    


