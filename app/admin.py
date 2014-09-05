from django.contrib import admin
from .models import Word

class WordAdmin(admin.ModelAdmin):
	list_display = ('english', 'spanish')


admin.site.register(Word, WordAdmin)

