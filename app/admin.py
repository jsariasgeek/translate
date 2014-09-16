from django.contrib import admin
from .models import Word

class WordAdmin(admin.ModelAdmin):
	list_display = ('english', 'spanish')
	list_per_page = 50
	# list_editable = ('spanish',)


admin.site.register(Word, WordAdmin)

