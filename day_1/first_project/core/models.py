from django.db import models

# Create your models here.
class Curso(models.Model):
	nome = models.CharField(max_length=255)
	codigo = models.CharField(max_length=5)

	class Meta:
		verbose_name = "Curso"
		verbose_name_plural = "Cursos"

	def __str__(self):
		return '{0} - {1}'.format(self.nome, self.codigo)

class Aluno(models.Model):
	nome = models.CharField(max_length=40)
	email = models.EmailField(max_length=40)
	cpf = models.CharField(max_length=14)
	curso = models.ForeignKey('Curso')
	rank = models.DecimalField(max_digits=3, decimal_places=2)
	data_nascimento = models.DateField()

	def __str__(self):
		return '{0}'.format(self.nome)

class Disciplina(models.Model):
	nome = models.CharField(max_length=100)
	codigo = models.CharField(max_length=5)
	curso = models.ForeignKey('Curso')
	data_de_insercao = models.DateField()

	tipo_eletiva = models.CharField(
        max_length=15,
        choices= (('perfil', 'Perfil'), ('livre', 'Livre'), ('obrigatoria', 'Obrigatoria')),
        default='obrigatoria'
    )

   