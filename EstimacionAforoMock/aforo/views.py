from rest_framework.decorators import api_view
from rest_framework.response import Response


aforos_rest = {
    "11": 40,
    "14": 40,
    "15": 40,
    "17": 40,
    "20-1": 40,
    "20-2": 40,
    "20-3": 40,
    "121": 40,
    "125": 40,
    "127": 40,
    "128": 40,
    "20-4": 40,
    "20-5": 40,
    "20-6": 40,
    "20-7": 40,
    "20-8": 40,
    "20-9": 40,
    "20-10": 40,
    "20-11": 40,
    "20-12": 40,
    "20-13": 40,
    "20-14": 40,
    "20-15": 40,
    "20-16": 40,
}

@api_view(["GET"])
def list(request):
    return Response(aforos_rest)

@api_view(["GET"])
def get(request, id_rest):
    return Response({"Aforo": aforos_rest[id_rest]})
