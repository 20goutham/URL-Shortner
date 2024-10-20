from django.db.models import Count
from .models import ClickAnalytics

def get_device_clicks(obj):
    device_clicks = ClickAnalytics.objects.filter(url=obj).exclude(device='Desktop').values('device').annotate(click_count=Count('id'))
    return {item['device']: item['click_count'] for item in device_clicks}

def get_country_clicks(obj):
    country_clicks = ClickAnalytics.objects.filter(url=obj).values('country').annotate(click_count=Count('id'))
    return {item['country']: item['click_count'] for item in country_clicks}
