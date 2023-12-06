from django.db import models

# Create your models here.
class dis(models.Model):
    name = models.CharField(max_length=50)
    img=models.ImageField(upload_to='pic')
    def __str__(self):
        return self.name
class booking(models.Model):
    date=models.DateField()
    pname=models.CharField(max_length=50)
    age=models.IntegerField()
    gender=models.CharField(max_length=50) 
    phone=models.CharField(max_length=50)
    name=models.ForeignKey(dis,on_delete=models.CASCADE)
    def __str__(self):
        return self.pname