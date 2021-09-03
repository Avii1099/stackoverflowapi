from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import serializers, settings, viewsets
from .models import Question
from .serializer import QuestionSerializer
from bs4 import BeautifulSoup
import requests
import json
from django.core.cache import cache
from ipware import get_client_ip

# Create your views here.

CASHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:    
        ip = request.META.get('REMOTE_ADDR')
    return ip

def rate_limiting(request):
    current_ip = get_client_ip(request)
    if cache.get(current_ip):
        total_calls = cache.get(current_ip)

        if total_calls >= 5:
              return JsonResponse({'status': 501, 'message':'time limit', 
                                        'time': f'try after {cache.ttl(current_ip)} seconds'}) 
        else:
            cache.set(current_ip, total_calls+1)
            return JsonResponse({'total calls ': total_calls})

    cache.set(current_ip, 1, timeout=60)

    return JsonResponse({'status': 200, 'ip': get_client_ip(request)})

def home(request):
    return HttpResponse('sussess')

class QuestionApi(viewsets.ModelViewSet):
    throttle_scope = 'djstackapi'
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

def latest(request):
    try:
        res = requests.get("https://stackoverflow.com/questions")

        soup = BeautifulSoup(res.text, "html.parser")

        questions = soup.select(".question-summary")
        for que in questions:
            q = que.select_one('.question-hyperlink').getText()
            vote_count = que.select_one('.vote-count-post').getText()
            views = que.select_one('.views').attrs['title']
            tags = [i.getText() for i in (que.select('.post-tag'))]

            question = Question()
            question.question = q
            question.vote_count = vote_count
            question.views = views
            question.tags = tags

            question.save()
        return HttpResponse("Latest Data Fetched from Stack Overflow")
    except e as Exception:
        return HttpResponse(f"Failed {e}")
    


