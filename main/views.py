from django.http.response import JsonResponse
from django.shortcuts import render
from json import dump, load

from django.urls.conf import path
# Create your views here.


def get_data() -> list:
    try:
        with open('data.json', 'r') as f:
            return load(f)
    except Exception as e:
        print(e)
        with open('data.json', 'w') as f:
            dump([], f, indent=4, sort_keys=True)


def dump_data(data: list):
    with open('data.json', 'w') as f:
        dump(data, f, indent=4, sort_keys=True)


def init(request):
    return JsonResponse(get_data(), safe=False)


def new(request, name: str, date: str):
    data = get_data()
    data.append({'name': name, 'date': date})
    dump_data(data)
    return JsonResponse(data, safe=False)

def rm(req,i:int):
    data =get_data()
    data.remove(data[i])
    dump_data(data)
    return JsonResponse(data,safe=False)