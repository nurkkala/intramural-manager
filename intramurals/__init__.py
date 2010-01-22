from django.shortcuts import render_to_response


def dish_out_template(request, file_name):
	return render_to_response(file_name)
