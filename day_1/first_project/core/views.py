from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	return HttpResponse("my first view")

def about(request):
	return render(request, 'core/about.html', {'nome':'Andrea', 'curso':'Computer Engineering', 'disciplinas':['IC2', 'TG', 'TAIA']})