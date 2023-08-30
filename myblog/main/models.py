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
    
    
    
    