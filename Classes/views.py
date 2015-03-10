# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from models import *

def index(request):
	postagem = Postagem.objects.all().order_by('-data')
	return render_to_response('index.html',{'post': postagem})
	