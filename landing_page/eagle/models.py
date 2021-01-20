from django.db import models

# Create your models here.
class Test(models.Model):
    Email = models.CharField(max_length=200)

# https://docs.djangoproject.com/ko/3.1/intro/tutorial02/
# python manage.py makemigrations sms
#  python manage.py migrate
# python manage.py createsuperuser
