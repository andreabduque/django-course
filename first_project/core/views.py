from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import MatriculaModelForm, LoginForm
from .models import Aluno
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,logout as auth_logout, login as auth_login


def home(request):
	return  render(request, 'home.html')

def logout(request):
	auth_logout(request)
	return redirect('/login')

class SignUpView(View):
	def get(self, request):
		form = MatriculaModelForm()
		return render(request, 'core/signup.html', {'form':form})

	def post(self, request):
		form = MatriculaModelForm(request.POST, request.FILES)
		if(form.is_valid()):
			print("eh valido")
			form.save()
			form = MatriculaModelForm()

			msg = "Cadastro efetuado com sucesso"

			return render(request, 'core/signup.html', {'form':form, 'msg':msg})

class ProfileView(View):
	def get(self, request):
		return profile(request)

	def post(self, request):
		pass

@login_required
def profile(request):
	return render(request, 'core/about.html', {'user':request.user, 'disciplinas':['IC2', 'TG', 'TAIA']})


class LoginView(View):

	def get(self, request):
		form = LoginForm()
		return render(request, 'core/login.html', {'form':form})

	def post(self, request):
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('email')
			password = form.cleaned_data.get('senha')

			user = authenticate(request, username=username, password=password)
			if user is not None:
				auth_login(request, user)
				return redirect('/profile')

			else:
				msg ='Email ou Senha Incorreto'
				return render(request, 'core/login.html', {'form':form, 'msg':msg})

class AlunoListView(ListView):
	model = Aluno
	# def get_context_data(self, **kwargs):
	# 	context = super(AlunoListView, self).get_context_data(**kwargs)
	#
	# 	if(request.user):
	# 		context['user'] = request.user
	#
	# 	return context

class AlunoDetailView(DetailView):
	model = Aluno
