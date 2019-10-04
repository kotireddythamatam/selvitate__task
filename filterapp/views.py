from django.shortcuts import render
from .models import FILE
from django.http import HttpResponse,HttpResponseRedirect

def file_upload(request):
    if request.method == "GET":
        return render(request,'file.html')
    else:
        csv_file = request.FILES["csv_file1"]
        file_data = csv_file.read().decode("utf-8")
        lines = file_data.split("\n")
        for line in lines:
            try:
                fields = line.split(",")
                obj = FILE(Product_Name=fields[0],Product_URL=fields[1],Reviews=fields[2],Review_Count=fields[3],Price=fields[4],Image_URL=fields[5],Category=fields[6],Sub_Category=fields[7])
                obj.save()
            except Exception as e:
                pass
        return HttpResponse('file uploaded successfully')

def display(request):
    if request.method == "GET":
        return render(request,'display.html')

def price_filter(request,value):
    if value == 500:
        obj = FILE.objects.filter(Price=500)
        return render(request,'display.html',{'obj':obj})
    elif value == 1000:
        obj = FILE.objects.filter(Price=1000)
        return render(request,'display.html',{'obj':obj})
    elif value == 2000:
        obj = FILE.objects.filter(Price=2000)
        return render(request,'display.html',{'obj':obj})
    elif value == 5000:
        obj = FILE.objects.filter(Price=5000)
        return render(request,'display.html',{'obj':obj})
    elif value == 10000:
        obj = FILE.objects.filter(Price=10000)
        return render(request,'display.html',{'obj':obj})

def rating_filter(request,value):
    if value == 1:
        obj = FILE.objects.filter(Reviews=str(1.0)+' out of '+str(5)+' stars')
        return render(request,'display.html',{'obj':obj})
    elif value == 2:
        obj = FILE.objects.filter(Reviews=str(2.0)+' out of '+str(5)+' stars')
        return render(request,'display.html',{'obj':obj})
    elif value == 3:
        obj = FILE.objects.filter(Reviews=str(3.0)+' out of '+str(5)+' stars')
        return render(request,'display.html',{'obj':obj})
    elif value == 4:
        obj = FILE.objects.filter(Reviews=str(4.0)+' out of '+str(5)+' stars')
        return render(request,'display.html',{'obj':obj})
    elif value == 5:
        obj = FILE.objects.filter(Reviews=str(5.0)+' out of '+str(5)+' stars')
        return render(request,'display.html',{'obj':obj})

def average_price(request):
    obj = FILE.objects.filter(Price=5000)
    return render(request,'display.html',{'obj':obj})

def average_rating(request):
    obj = FILE.objects.filter(Reviews=str(3.0)+' out of '+str(5)+' stars')
    return render(request,'display.html',{'obj':obj})
