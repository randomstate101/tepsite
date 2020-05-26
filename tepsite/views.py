from django.shortcuts import render
from django.http import HttpResponse

def index(Request):
	return HttpResponse("Homepage")


def details(request,question_id):
	return HttpResponse("You are currently viewing %s." %question_id)


def responses(request,question_id):
	response = "You are looking at the Responses of Question %s."
	return HttpResponse(response %question_id)

	