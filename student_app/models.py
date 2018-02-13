from django.db import models
from django.utils import timezone

# Create your models here.

class School(models.Model):
	rating = (
		('1','1'),
		('2','2'),
		('3','3'),
		('4','4'),
		('5','5'),		
		)

	name = models.CharField(verbose_name='School Name', max_length = 50)
	address = models.TextField(null=True, blank=True)
	rating = models.CharField(choices=rating, max_length = 10)
	email = models.EmailField()
	contact_no = models.BigIntegerField(verbose_name='Contact No.', max_length = 13, null=True, blank=True)
	website = models.CharField(max_length = 50, null=True, blank=True)
	enabled = models.BooleanField(default=True)
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = "School"
		verbose_name_plural = "School"

	def __str__(self):
		return self.name

class Student(models.Model):
	standard = (
		('5','5'),
		('6','6'),
		('7','7'),
		('8','8'),
		('9','9'),
		('10','10'),
		)

	school = models.ForeignKey(School)
	first_name = models.CharField(max_length = 25)
	last_name = models.CharField(max_length = 25)
	image = models.ImageField(upload_to = 'student_image/', null=True, blank=True)
	email = models.EmailField()
	residental_address = models.TextField(null=True, blank=True)
	standard = models.CharField(choices=standard, max_length = 10)
	roll_no = models.IntegerField(null=True, blank=True)
	fees = models.IntegerField(null=True, blank=True)
	enabled = models.BooleanField(default=True)
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = "Student"
		verbose_name_plural = "Student"

	def __str__(self):
		return self.first_name
