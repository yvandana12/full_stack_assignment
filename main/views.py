from django.shortcuts import render
import json
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.

def jsonData(day,time1, time2):
    
    #i just opened up jso file and compared the input values with slot avalable and printed slot available in index.html page for now
    # i have not done any string formatting to match time range properly kindly fill in test cases data as in json file 9 AM 10Am
    json_data=open("C:\\Users\\DELL\\Desktop\\placement\\backend\\slotbooking\\main\\availibility.json")
    data1=json.load(json_data)  #convertung to dictionary
    #print(type(data1))
    for k1 in data1:
        
        if(k1=="availability"):
            for k2,v2 in data1[k1].items():
                if(k2==day):
                    #if the entered day matches
                    for l in v2:
                        print(time1)
                        print(l['start_time']+" "+l['end_time'])
                        if l['start_time']==time1 and l['end_time']==time2:
                            return True

    return False                                

  
def bookSlot(day,time1, time2):
    """
    i am thinking of changing availibility data in json file itself if the slot is avaialble
    so i have removed that particular entry which match to user requirement 
    to make this slot not available for other user
    """
    json_data=open("C:\\Users\\DELL\\Desktop\\placement\\backend\\slotbooking\\main\\availibility.json","r+")   #opening file in read write mode
    data1=json.load(json_data)  #convertung to dictionary
    #print(type(data1))
    for k1 in data1:
        
        if(k1=="availability"):
            for k2,v2 in data1[k1].items():
                if(k2==day):
                    #if the entered day matches
                    for l in v2:
                        print(l['start_time']+" "+l['end_time'])
                        if l['start_time']==time1 and l['end_time']==time2:
                            #here write logic for changing data
                            v2.remove(l)
                            # l['start_time']=0
                            # l['end_time']=0
                            return True

    return False                                
def book(request):
    pass

def index(request):
    context={}
    """
    this function will check if required prefrences are available or not if available will redirect to book.html page
    """
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        day=request.POST.get('day')
        time1=request.POST.get('time1')
        time2=request.POST.get('time2')
        if(jsonData(day,time1, time2)):
            print("Slot available ")
            messages.info(request,'Slot is available')
            return render(request, 'book.html', {'status': "available","name":name, "email":email, "address":address, "day":day,"time1":time1, "time2":time2})
        else:
            print("Slot Not available ")
            messages.info(request,'Slot is not available')
            context["status"]=" not available"
            
            return render(request, 'index.html', {'status': " not available"})

    return render(request, 'index.html', context)

def result(request):
    return render(request, 'index.html')

