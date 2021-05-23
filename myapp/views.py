"""
    Author: Akshat Trivedi
    Python Version: 3.9.2
"""

from django.shortcuts import render
from myapp.notifierService import NotifierService
    
notifierService = NotifierService()


def index(request):

    # if request.GET.get('state'):
    if request.method == "POST":
        return render(request,'myapp/index.html')
    else:
        states = notifierService.getAllStates()
        districts = notifierService.getAllDistricts("Madhya Pradesh")
        ages = notifierService.getAllAges()
        vaccines = notifierService.getAllVaccines()
        doses = notifierService.getAllDoses()
        context = { "states": states, "ages": ages, "districts" : districts, "vaccines": vaccines, "doses": doses}
        return render(request,'myapp/index.html',context)
    


