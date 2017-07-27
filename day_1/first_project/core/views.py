from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.base import TemplateView
from .forms import MatriculaModelForm, LoginForm
from .models import Aluno
from django.contrib.auth import authenticate,logout as auth_logout, login as auth_login


# Create your views here.
# def home(request):
# 	return HttpResponse("my first view")


class HomeView(TemplateView):
	template_name = 'core/home.html'

	def get_context_data(self, **kwargs):
		context = super(HomePageView, self).get_context_data(**kwargs)

		if(request.user):
			context['user'] = request.user

		context['msg'] = 'essa msg aparece no front'
		return context

def signup(request):
	form = MatriculaModelForm()
	msg = None

	if(request.method == 'POST'):
		form = MatriculaModelForm(request.POST)

		if(form.is_valid()):
			print("eh valido")
			form.save()
			form = MatriculaModelForm()

			msg = "Cadastro efetuado com sucesso"

			return render(request, 'core/signup.html', {'form':form, 'msg':msg})

	return render(request, 'core/signup.html', {'form':form, 'msg':msg})

class SignUpView(View):
	def get(self, request):
		form = MatriculaModelForm()
		msg = None
		return render(request, 'core/signup.html', {'form':form, 'msg':msg})

	def post(self, request):
		form = MatriculaModelForm(request.POST)

		if(form.is_valid()):
			print("eh valido")
			form.save()
			form = MatriculaModelForm()

			msg = "Cadastro efetuado com sucesso"

			return render(request, 'core/signup.html', {'form':form, 'msg':msg})

class ProfileView(View):
	def get(self, request):
		return render(request, 'core/about.html', {'nome':'Andrea', 'curso':'Computer Engineering', 'disciplinas':['IC2', 'TG', 'TAIA']})

	def post(self, request):
		pass

def about(request):
	form = MatriculaModelForm()
	msg = None

	if(request.method == 'POST'):
		form = MatriculaModelForm(request.POST)

		if(form.is_valid()):
			print("eh valido")
			form.save()
			form = MatriculaModelForm()

			msg = "Cadastro efetuado com sucesso"

			return render(request, 'core/about.html', {'nome':'Andrea', 'curso':'Computer Engineering', 'disciplinas':['IC2', 'TG', 'TAIA'], 'form':form, "msg":msg})

	return render(request, 'core/about.html', {'nome':'Andrea', 'curso':'Computer Engineering', 'disciplinas':['IC2', 'TG', 'TAIA'], 'form':form})

# @login_required
# def profile(request):
# 	return render(request, 'core/profile.html', {'user':request.user})


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
			print("USER")
			print(user)
			if user is not None:
				auth_login(request, user)
				print("reocnheu user")
				return redirect('profile')
				# return HttpResponse("autenticou")

			else:
				msg ='Email ou Senha Incorreto'
				return render(request, 'core/login.html', {'form':form, 'msg':msg})
