from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=256)
    
    def __str__(self):
        return self.name
    
class Article(models.Model):
    # articleno.-->in future we create a primary key -->django gives us  a primarykey alias pk 
    title= models.CharField(max_length= 256)
    content= models.TextField()
    created_at= models.DateTimeField(auto_now_add = True) 
    
    author= models.ManyToManyField('Author')
    
    def __str__(self):
        return self.title
    
class Student(models.Model):  
    name=models.CharField(max_length=256)
    roll_number=models.IntegerField(unique=True)
    college=models.ForeignKey('college',on_delete=models.CASCADE)    
    def __str__(self):
        return self.name

class College(models.Model):
    name=models.CharField(max_length=256)
    def __str__(self):
        return self.name
    
    