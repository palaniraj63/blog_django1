from django.urls import path    
from main import views
urlpatterns=[
   
    path('',views.index,name= 'index'),
    path('atlas',views.Atlas.as_view()),
    path('college/<int:pk>',views.CollegeDetail.as_view(),name= "college" ),
    path('college',views.CollegeList.as_view()),
    path('forms',views.formchecker,name= 'formchecker'),
    path('article/<int:pk>',views.article, name='get_article'),
    path('author/<int:pk>',views.author, name='get_author'),
    path('article',views.create_article,name='create_article')
]
