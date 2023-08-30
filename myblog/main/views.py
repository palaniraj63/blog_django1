from django.shortcuts import render ,get_object_or_404 ,get_list_or_404
from main import models
from django.http import Http404 

from main import forms #this is for importing forms if u have any 
# from django import forms
# Create your views here.

#these all should come in controllers.py mostly 
def index(request):
    
    # latest_articles= models.Article.objects.all()[:10] #this is models it is saved as objectsin table and that is limit tp 10 #this  has str dunder set to title when we access in  html it will print the title 
    latest_articles=models.Article.objects.all().order_by('-created_at')[:10] #rderby query same as sql # - is used to escending 
    context={"latest_articles":latest_articles}
    return render(request,'main/index.html',context)

def article(request, pk):
    # article =models.Article.object.get(pk = pk)
    # try: 
    #     article = models.Article.objects.get(pk=pk) #objects if u write object u may face erroe this is for exception handlingh 
    # except:
    #    raise Http404()
    article = get_object_or_404(models.Article,pk=pk) #pk object is the primary key 
     
    context={
            "article":article
        }  
    return render(request,'main/article.html',context)

def author(request, pk):    
    
    author =get_object_or_404(models.Author,pk=pk)
    context={
            "author":author
        }  
    return render(request,'main/authour.html',context)

def create_article(request):
    print(request.POST)
    authors = models.Author.objects.all()
    context={ "authors":authors}
    if request.method =="POST":
        article_data ={
        'title':request.POST['title'],
        'content':request.POST['content']
     }
    article=models.Article.objects.create(**article_data) #creating a new model object 
    author=models.Author.objects.filter(pk =request.POST['author'])
    article.authors.set(author)
    #  author=models.Author.objects.get(pk =request.POST['author']) we can use any one above or below 
    # article.authors.set([author])
    context["success"] =True
    
    return render(request,'main/create_article.html',context)

def formchecker(request):
    context={ "form" : forms.ExampleForm()}
    return render(request,'main/form.html',context)
