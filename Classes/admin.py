# -*- coding:utf-8 -*-
from django.contrib import admin
from models import *

class AdminPostagem(admin.ModelAdmin):
	 list_display = ['titulo','postagem','data']
	 list_filter = ['data']
	 search_fields = ['titulo']
	 

class AdminEnquete(admin.ModelAdmin):
	 list_display = ['enquete','data']
	 list_filter = ['data']
	 search_fields = ['enquete']

admin.site.register(Postagem, AdminPostagem)
admin.site.register(Enquete, AdminEnquete)