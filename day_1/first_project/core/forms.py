from django import forms
from .models import Curso, Aluno
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# class MatriculaForm(forms.Form):
#     nome= forms.CharField(max_length=100)
#     cpf= forms.CharField(max_length=14)
#     email = forms.EmailField(max_length=25)
#     data_nascimento = forms.DateField()
#     curso = forms.ModelChoiceField(queryset=Curso.objects.all())
#
#     def save(self):
#     	data = self.cleaned_data
#     	novo_aluno = Aluno(**data)
#     	novo_aluno.save()
#     	return novo_aluno

class LoginForm(forms.Form):
	email = forms.CharField()
	senha = forms.CharField(widget=forms.PasswordInput())

class MatriculaModelForm(forms.ModelForm):
    email = forms.EmailField()
    senha = forms.CharField(widget=forms.PasswordInput())
    #Redefinir os campos com o atributo label=
    #para remover *

    class Meta:
        model = Aluno
        fields = ['nome', 'cpf', 'curso', 'email', 'senha']

    def clean(self):
        #import pdb; ipdb.set_trace()
        data = super(MatriculaModelForm, self).clean()
        if(User.objects.filter(username=data.get('email')).count() > 0):
            raise ValidationError('Username ja usado', code='invalid_username')

        return data

    def save(self, *args, **kwags):
        user = User.objects.create_user(self.cleaned_data.get('email'), self.cleaned_data.get('email'), self.cleaned_data.get('senha'))
        self.instance.user = user
        self.instance.rank = 5
        return super(MatriculaModelForm, self).save(self)
