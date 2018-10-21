from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from users.models import Users, Plants, Members, Vehicles
from .models import reservoir, reservoirdata, weathersensors, plantsensors
from django.views import generic
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import time

import time

userid = -1
plant_id = -1


@method_decorator(csrf_exempt, name='dispatch')
class sensor_data(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('this is a get request')

    def post(self, request, *args, **kwargs):
        rain = request.POST.get("rain", "")
        temp = request.POST.get("temp", "")
        humidity = request.POST.get("humidity", "")

        soilmoist = request.POST.get("soilmoist", "")

        distance = request.POST.get("distance", "")
        ph = request.POST.get("ph", "")
        turbidity = request.POST.get("turbidity", "")

        user_id = request.POST.get("user_id", "")
        volume = request.POST.get("volume", "")
        reservoir_id = request.POST.get("reservoir_id", "")
        
        if float(soilmoist) < 0:
            soilmoist = str(0)
        
        p = Users.objects.filter(id=user_id)[0]
        w = weathersensors(rain = rain, temp = temp, humidity = humidity, userid = user_id, time = time.strftime("%X"), date = time.strftime("%Y-%m-%d"))
        w.save()
        entryid = w.id
        s = weathersensors.objects.filter(pk=w.id)[0]
        rd = reservoir.objects.filter(pk=reservoir_id)[0]
        p = plantsensors(entryid = s, soilmoisture = soilmoist)
        p.save()
        r = reservoirdata(entryid = s, reservoirid = rd, distance = distance, ph = ph, turbidity = turbidity)
        r.save()
        rd.volume += float(volume)
        rd.save()
        return HttpResponse('DONE')

def show_list(request):
    print("hello i am here")
    if 'name' in request.session:
        global userid
        userid = request.session['id']
        print(userid)
        s = Users.objects.filter(pk = userid)
        z = Plants.objects.filter(userid = s)
        m = Members.objects.filter(userid = s)
        v = Vehicles.objects.filter(userid = s)
        r = reservoir.objects.filter(userid = s)
        f = Users.objects.filter(id = userid)
        return render(request, 'sensors/temperature.html', {"userdata": f[0],  "reservoir_names": r, "plant_names" : z, "vehicle_name": v, "member_names" : m, "plant_count": s[0].plantcount, "member_count": s[0].membercount, "vehicle_count": s[0].vehicleCount})
    else:
        return redirect('../../users/login')

def setreservoir(request):
    if request.POST:
        global userid
        z = Users.objects.filter(id=userid)[0]
        global plantid
        plantid = z.currentplant
        z.currentreservoir = request.POST['currentplant']
        z.save()
    return redirect('../data')

def data_update(request):
    global userid
    p = Users.objects.filter(id = userid)[0]

    li = weathersensors.objects.filter(userid=userid)
    print(li)
    if li.count():
        entry = li[li.count()-1].id
        c = weathersensors.objects.filter(id = entry)
        d = plantsensors.objects.filter(entryid = entry)
        e = reservoirdata.objects.filter(entryid = entry)
        print("rain",c[0].rain)
        print(d)
        print(e)
        data = {
            'temp' : c[0].temp,
            'humidity' : c[0].humidity,
            'userid' : c[0].userid,
            'date' : c[0].date,
            'time' : c[0].time,
            'soilmoist' : d[0].soilmoisture,
            'distance' : e[0].distance,
            'data' : 1,
            'rain': c[0].rain
        }
        return JsonResponse(data)
    else:
        data = {
            'data' : 0
        }
        return JsonResponse(data)


def DetailView(request, pid):
    global userid
    print(pid)
    w = reservoirdata.objects.filter(reservoirid = pid)
    print(w.count())
    # if w.count() >= 10:
        # temp = []
        # humidity = []
        # time = []
        # date = []
        # soilmoisture = []
        # distance = []
        # actualheight = []
        # ph = []
        # turbidity = []
    #     i = 0
    #     for i in range(10):
    #         distance.append(w[i].distance)
    #         temp.append(w[i].ph)
    #         soilmoisture.append(w[i].turbidity)
        
        # context = {
        #         'temp' : temp,
        #         'humidity' : humidity,
        #         'date' : date,
        #         'time' : time,
        #         'soilmoist' : soilmoisture,
        #         'distance' : distance,
        #         'pid' : pid,
        #         'data' : 1
        #     }
    #     return render(request, 'sensors/detail.html',context)   
    # else:
    #     context = {
    #         'data' : 0
    #     }

    temp = []
    humidity = []
    time = []
    date = []
    soilmoisture = []
    distance = []
    ph = []
    turbidity = []
    for i in range(w.count()):
        distance.append((3.14*(abs(12-w[i].distance)%12)*9)/1000)
        temp.append(w[i].ph)
        soilmoisture.append(w[i].turbidity)

    if w.count() < 10:
        for i in range(w.count(), 10):
            distance.append(0)
            temp.append(0)
            soilmoisture.append(0)

    context = {
                'temp' : temp,
                'date' : date,
                'time' : time,
                'soilmoist' : soilmoisture,
                'distance' : distance,
                'pid' : pid,
                'data' : 1
            }


    return render(request, 'sensors/detail.html',context)


# -------------------- MOBILE APP ----------------------
@csrf_exempt
def drinking(request):
    if request.method=='POST':
        jsonResponse=json.loads(request.body.decode('utf-8'))
        id=jsonResponse['id']
        res=jsonResponse['res']
        print(id,res)

        w = reservoirdata.objects.filter(reservoirid = res)
        print(w.count())

        temp = []
        humidity = []
        time = []
        date = []
        soilmoisture = []
        distance = []
        ph = []
        turbidity = []
        k=1
        i=w.count()-1
        while i>=0 and k<=10:
            print(i)
            distance.append((3.14*(abs(12-w[i].distance)%12)*9)/1000)
            temp.append(w[i].ph)
            soilmoisture.append(w[i].turbidity)
            k=k+1
            i-=1

        if w.count() < 10:
            for i in range(w.count(), 10):
                distance.append(0)
                temp.append(0)
                soilmoisture.append(0)

        context = {
                    'temp' : temp,
                    'date' : date,
                    'time' : time,
                    'soilmoist' : soilmoisture,
                    'distance' : distance,
                    'data' : 1
                }
        return JsonResponse(context);
