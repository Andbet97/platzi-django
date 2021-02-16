"""Platzigram views."""
# Django
from django.http import HttpResponse, JsonResponse

# Utils
from datetime import datetime
import json


def hello(request):
    """Hello world."""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh hi! Current time is {}'.format(str(now)))


def hi(request):
    """Hi."""
    numbers = request.GET['numbers']
    numbers = sorted([int(i) for i in numbers.split(',')])
    data = {
        'status': 'Ok',
        'data': numbers
    }
    return HttpResponse(
        json.dumps(data, indent=4), 
        content_type='application/json'
    )
    # return JsonResponse(data)
