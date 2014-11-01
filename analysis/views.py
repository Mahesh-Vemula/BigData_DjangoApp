from django.shortcuts import render

# Create your views here.
def home(request):
	context = {}
 	template = "index.html"
 	return render(request, template, context)


def about(request):
	context = {}
 	template = "about.html"
 	return render(request, template, context)

def map(request):
	context = {}
 	template = "mapanalysis.html"
 	return render(request, template, context)

def chart(request):
	context = {}
 	template = "chartanalysis.html"
 	return render(request, template, context)