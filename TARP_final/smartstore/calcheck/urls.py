from django.urls import path
from . import views

urlpatterns =[
    path('home/', views.home),
    path('home/title/', views.upload_csv),
    path('home/title/results',views.results),
    path('home/title/results/energyviz',views.doughnut_chart),
    path('home/title/results/energyviz/satunsat',views.fats_viz),
    path('home/title/results/energyviz/satunsat/cholesterol',views.cholest_viz),
    path('home/title/results/energyviz/satunsat/cholesterol/cartotal',views.cart_viz),
    path('home/title/results/energyviz/satunsat/cholesterol/cartotal/cartsum',views.cart_summary)

]