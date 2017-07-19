from django.db import models

# Create your models here.
class Curso(models.Model):
	nome = models.CharField(max_length=255)
	codigo = models.CharField(max_length=5)

	class Meta:
		verbose_name = "Curso"
		verbose_name_plural = "Cursos"

	def __str__(self):
		return '{0}'.format(self.nome)