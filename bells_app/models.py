from django.db import models

# Create your models here.
class Contact(models.Model):
	name = models.CharField(max_length=300, blank=False, null=False)
	email = models.EmailField(max_length=300, blank=False, null=False)
	message = models.TextField(blank=False, null=False)

	def __str__(self):
		return f'{self.name}, {self.email}'

class Course(models.Model):
	name = models.CharField(max_length=400)
	cut_off_mark = models.IntegerField()

	def __str__(self):
		return self.name


class Admission_List(models.Model):
	name = models.CharField(max_length=300, blank=False, null=False)
	email = models.EmailField(max_length=300, blank=False, null=False)
	phone = models.CharField(max_length=300)
	course = models.ForeignKey(Course, on_delete=models.CASCADE)

	def __str__(self):
		return self.name
