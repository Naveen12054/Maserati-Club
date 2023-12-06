from .import views 
from django.urls import path
urlpatterns = [
    path('',views.index,name='index'),
    path('display/',views.display,name='display'),
    path('book/',views.books,name='book'),
    path('games/',views.games,name='games'),
    path('about/',views.about,name='about'),
]
