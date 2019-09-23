from django.db import models
from django.utils import timezone

# Create your models here.
class stockinput(models.Model):
	name = models.CharField(max_length = 40)
	mobile = models.IntegerField()
	address = models.CharField(max_length=100)
	bloodgroup = models.CharField(max_length=5)

class requestClass(models.Model):
	name_request = models.CharField(max_length=40)
	mobile_request = models.IntegerField()
	address_request = models.CharField(max_length=100)
	email_request = models.CharField(max_length=30)
	bloodgroup_request = models.CharField(max_length=5)
	dateline_request = models.DateField(default=timezone.now().date())

		
class donated(models.Model):
	donate_name = models.CharField(max_length=100) 
	donate_mobile = models.IntegerField()
	donate_address = models.CharField(max_length=50)
	donate_email = models.CharField(max_length=50)
	donate_bloodgroup = models.CharField(max_length=5)
		

	
		
	
		
	
		