#Views without Django rest frameworks

import json

from django.http import  HttpResponse

from djangoProject_start.models import User


def hello(request):
    return HttpResponse("Welcome to My First Django Project")

def hello_withName(request, name):
    return HttpResponse(f"Welcome to My First Django Project, %s" % name)

def thankYou(request):
    return HttpResponse("Thank you for visiting My First Django Project")

def user(request) -> HttpResponse:
    if request.method == "GET":
        user = User.objects.all()
        serializer = [user.id for user in user]
        result = json.dumps(serializer)
        return HttpResponse(result)

    if request.method == "POST":
        body = json.loads(request.body)
        user = User(name=body["name"], age=body["age"],email=body["email"])
        user.save()
        return  HttpResponse(user.name, status=200)
    else:
        return HttpResponse("Method Not Allowed")

def users(request, id) -> HttpResponse:
    if request.method == "PUT":
        body = json.loads(request.body)
        user = User.objects.get(id=id)
        user.name = body["name"]
        user.age = body["age"]
        user.email = body["email"]
        user.save()
        return HttpResponse(user.name, "message updated", status=200)

    if request.method == "DELETE":
        user = User.objects.get(id=id)
        user.delete()
        return HttpResponse(user.name, "message deleted", status=200)

    else:
        return HttpResponse("Method Not Allowed")
