from django.http import HttpResponse
from django.shortcuts import render
from register_device.models import device

# Create your views here.
def dashboard(request):
    deviceData = device.objects.all()
    
    data = {
        'key': deviceData
    }
    return render(request,'dashboard.html',data)

def form(request):
    return render(request,'reg_form.html')

def saveData(request):
    if request.method == "POST":
        id = request.POST.get('Id')
        DeviceType = request.POST.get('DeviceType')
        DeviceVersion = request.POST.get('DeviceVersion')
        DeviceLocation = request.POST.get('DeviceLocation')
        PrimaryGroup = request.POST.get('PrimaryGroup')
        SecondaryGroup = request.POST.get('SecondaryGroup')
        en = device(Id=id, DeviceType=DeviceType,
                    DeviceVersion=DeviceVersion, DeviceLocation=DeviceLocation, PrimaryGroup=PrimaryGroup, SecondaryGroup=SecondaryGroup)
        en.save()
    return render(request,'reg_form.html')
