from django import forms
from .models import Curso, Aluno
from django.contrib.auth.models import User

class MatriculaForm(forms.Form):
    nome= forms.CharField(max_length=100)
    cpf= forms.CharField(max_length=14)
    email = forms.EmailField(max_length=25)
    data_nascimento = forms.DateField()
    curso = forms.ModelChoiceField(queryset=Curso.objects.all())

    def save(self):
    	data = self.cleaned_data
    	novo_aluno = Aluno(**data)
    	novo_aluno.save()
    	return novo_aluno


class MatriculaModelForm(forms.ModelForm):
	email = forms.EmailField()
	senha = forms.CharField(widget=forms.PasswordInput())

	class Meta:                                                                                                                                                          
		model = Aluno
		fields = ['nome', 'cpf', 'curso', 'email', 'senha']

	def clean(self):
		#import pdb; ipdb.set_trace()
		data = super(MatriculaModelForm, self).clean()
		user = User.objects.create_user()

	def save(self, *args, **kwags):
		self.instance.rank = 5
		return super(MatriculaModelForm, self).save(self)

