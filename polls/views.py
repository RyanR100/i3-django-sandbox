from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello World!  You're at the polls index page!")

def results(request, question_id):
    response =  "You're looking for results for question with id %s"
    return HttpResponse(response % question_id)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s" % question_id)

def vote(request, question_id):
    return HttpResponse("Your're voting on question %s." % question_id)

