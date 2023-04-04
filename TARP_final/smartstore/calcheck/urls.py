from django.urls import path
from . import views

urlpatterns =[
    path('home/', views.home),
    path('home/title/', views.upload_csv),
    path('home/title/results',views.results),
    path('home/title/results/energyviz',views.doughnut_chart)
]