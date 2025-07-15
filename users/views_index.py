from django.http import HttpResponse
from django.conf import settings
import os

def index(request):
    with open(os.path.join(settings.BASE_DIR, 'index.html'), 'r', encoding='utf-8') as f:
        return HttpResponse(f.read())
