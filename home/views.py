from django.shortcuts import render
from datetime import datetime
from home.models import Result

# Create your views here.
def index(request):
    if request.method == "POST":
        age = request.POST.get('age')
        sex = request.POST.get('sex')
        temperature = request.POST.get('temperature')
        symptoms = request.POST.get('symptoms')
        addi_symptoms = request.POST.get('addi_symptoms')


        result = Result(age=age, sex=sex, temperature=temperature, assessment_date=datetime.today(), assessment_score=4, covid19_result= 'Negative')
        result.save()

    
    
    return render(request, "index.html")

def result(request):

    return render(request, "index.html")