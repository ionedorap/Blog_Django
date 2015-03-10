# -*- coding:utf-8 -*-
from django.db import models

class Postagem(models.Model):
	titulo = models.CharField('Título da Postagem',max_length = 50)
	postagem = models.TextField('Postagem')
	data = models.DateTimeField('Data da Postagem')

	def __unicode__ (self):
		return unicode("%s - %s - %s") % (self.titulo, self.postagem, self.data)
		

class Enquete(models.Model):
	enquete = models.CharField('Enquete',max_length = 100)
	data = models.DateTimeField('Data da Enquete')

	def __unicode__ (self):
		return unicode("%s - %s") % (self.enquete, self.data)