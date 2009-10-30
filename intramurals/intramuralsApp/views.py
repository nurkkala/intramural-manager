# Create your views here.
from django.shortcuts import render_to_response
from django.template import Template, Context
from django.http import HttpResponse

def say_hi(request, name):
	t = Template("<html><body>Well hi there {{ name_of_person }}!</body></html>")
	c = Context({'name_of_person': name})
	html = t.render(c)
	return HttpResponse(html)

def dish_out_template(request, file_name):
	return render_to_response(file_name)
	
def index(request):
    return render_to_response("home.html")
