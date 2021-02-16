"""Platzigram views."""
# Django
from django.http import HttpResponse, JsonResponse

# Utils
from datetime import datetime


def hello(request):
    """Hello world."""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh hi! Current time is {}'.format(str(now)))


def hi(request):
    """Hi."""
    numbers = request.GET['numbers']
    numbers = numbers.split(',')
    numbers = [int(i) for i in numbers]
    numbers.sort()
    return JsonResponse({'sorted': numbers})
