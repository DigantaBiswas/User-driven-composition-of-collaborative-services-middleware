from django.db import models
from datetime import datetime
from django.utils import timezone


# Create your models here.
class Actuator(models.Model):
	topic = models.CharField(max_length=100, null = True)
	value = models.CharField(max_length=100, null = True)
	time = models.DateTimeField(auto_now_add=True,null = True)
	name = models.CharField(max_length=60, null = True)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
	
		if not self.id:
			self.time = timezone.now()
		return super(Actuator, self).save(*args, **kwargs)


class LowerSensor(models.Model):
	topic = models.CharField(max_length=100, null = True)
	value = models.CharField(max_length=100, null = True)
	time = models.DateTimeField(default=datetime.now, null=True)
	name = models.CharField(max_length=60, null = True)

	def __str__(self):
		return self.name
	def save(self, *args, **kwargs):
	
		if not self.id:
			self.time = timezone.now()
		return super(LowerSensor, self).save(*args, **kwargs)