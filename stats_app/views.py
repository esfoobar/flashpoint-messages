from django.http import JsonResponse

from stats_app.models import CityStats, UserStats

def stats_get(request):
    city_count = CityStats.objects.all().count()
    user_count = UserStats.objects.all().count()
    result = "success" # here we'd check some conditions
    
    return JsonResponse({
        'result': result,
        'cities': city_count,
        'users': user_count
        })