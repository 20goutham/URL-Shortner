from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import LongToShort, ClickAnalytics
from user_agents import parse
from django.db.models import Count
from .analytics import get_device_clicks, get_country_clicks

def hello_world(request):
    return HttpResponse('Hello world')

def home_page(request):
    context = {
        "submitted": False,
        "error": False
    }
    if request.method == 'POST':
        data = request.POST
        long_url = data.get('longurl')
        custom_name = data.get('custom_name')

        try:
            obj = LongToShort(long_url=long_url, short_url=custom_name)
            obj.save()
            context.update({
                "long_url": long_url,
                "short_url": request.build_absolute_uri() + custom_name,
                "date": obj.date,
                "clicks": obj.clicks,
                "submitted": True
            })
        except Exception as e:
            print(f"Error saving URL: {e}")
            context["error"] = True
    else:
        print("'User not sending anything'")

    return render(request, 'index.html', context)

def redirect_url(request, short_url):
    obj = get_object_or_404(LongToShort, short_url=short_url)
    long_url = obj.long_url
    obj.clicks += 1
    obj.save()

    user_agent = request.META.get('HTTP_USER_AGENT', '')
    user_agent_parsed = parse(user_agent)
    device = user_agent_parsed.device.family

   
    if device.lower() != "mobile":
        device = "PC"

    country = request.META.get('HTTP_CF_IPCOUNTRY', 'Unknown')  

    ClickAnalytics.objects.create(url=obj, device=device, country=country)

    return redirect(long_url)

def all_analytics(request):
    rows = LongToShort.objects.all()
    context = {
        "rows": rows 
    }
    return render(request, "all_analytics.html", context)

def analytics(request, short_url):
    obj = get_object_or_404(LongToShort, short_url=short_url)
    
    
    device_clicks = get_device_clicks(obj)
    country_clicks = get_country_clicks(obj)

 
    all_devices = ['PC', 'Mobile']
    
    for device in all_devices:
        if device not in device_clicks:
            device_clicks[device] = 0  

    context = {
        "long_url": obj.long_url,
        "clicks": obj.clicks,
        "device_clicks": device_clicks,
        "country_clicks": country_clicks,  
    }
    
    return render(request, "analytics.html", context)

def task(request):
    abs = {
        "my_name": "Goutham",
        "x": 10
    }
    return render(request, 'test.html', abs)
