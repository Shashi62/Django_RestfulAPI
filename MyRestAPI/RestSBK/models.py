from django.db import models

# Create your models here.


class Employee(models.Model):
    sno = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    emp_id = models.IntegerField()

    def __str__(self):
        return self.first_name
