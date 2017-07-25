from django.shortcuts import render
from django.http import HttpResponse
from .forms import MatriculaModelForm, MatriculaModelForm
from .models import Aluno

# Create your views here.
def home(request):
	return HttpResponse("my first view")

def about(request):
	form = MatriculaModelForm()


	if(request.method == 'POST'):
		form = MatriculaModelForm(request.POST)

		if(form.is_valid()):
			novo_aluno = Aluno(**form.cleaned_data)
			novo_aluno.save()

			form = MatriculaModelForm()
			msg = "Cadastro efetuado com sucesso"

		return render(request, 'core/about.html', {'nome':'Andrea', 'curso':'Computer Engineering', 'disciplinas':['IC2', 'TG', 'TAIA'], 'form':form, "msg":msg})




	return render(request, 'core/about.html', {'nome':'Andrea', 'curso':'Computer Engineering', 'disciplinas':['IC2', 'TG', 'TAIA'], 'form':form})