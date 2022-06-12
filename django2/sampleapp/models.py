from django.db import models

# Create your models here.
class Sample(models.Model):
    id=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    sName=models.CharField(max_length=20,null=False)
    sSex=models.CharField(default='M', max_length=2,null=False)
    sEmail=models.EmailField(blank=True, default='', max_length=100)
    sPhone=models.CharField(blank=True, default='', max_length=50)
    sAddr=models.CharField(blank=True, default='', max_length=255)
    def __str__(self):
        return self.sName
