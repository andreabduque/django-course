from django import forms
from .models import Curso, Aluno
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

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
        fields = ['nome', 'cpf', 'curso', 'email', 'senha', 'foto']

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
