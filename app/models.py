from django.db import models

class Word(models.Model):
	english = models.CharField(max_length=30)
	spanish = models.CharField(max_length=120)

	def __unicode__(self):
		return self.english