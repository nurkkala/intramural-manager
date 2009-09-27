# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse

def dish_out_template(request, file_name):
	return render_to_response(file_name)
	
