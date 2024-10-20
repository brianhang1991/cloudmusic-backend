# from django.shortcuts import render
import json

from django.http import HttpResponse

from djangoProject.db.sqlite_music_dao import get_musics
from djangoProject.models.http.music import object_2_json


# Create your views here.

def index(request):
    return HttpResponse("HelloDjango!")

def list_musics(request):
    return HttpResponse(json.dumps(get_musics(), default=object_2_json))



