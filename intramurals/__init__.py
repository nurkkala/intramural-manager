from django.shortcuts import render_to_response
from django.http import HttpResponse

def foo(request):
	return HttpResponse("foo")

def dish_out_template(request, file_name):
	return render_to_response(file_name)
