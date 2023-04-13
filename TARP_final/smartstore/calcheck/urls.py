from django.urls import path
from . import views
from .views import ProductListView

urlpatterns =[
    path('home/', views.home),
    path('home/title/', views.upload_csv),
    path('home/title/cartlist/', ProductListView.as_view(), name='cartlist'),
    path('home/title/cartlist/results',views.results),
    path('home/title/cartlist/results/energyviz',views.doughnut_chart),
    path('home/title/cartlist/results/energyviz/satunsat',views.fats_viz),
    path('home/title/cartlist/results/energyviz/satunsat/cholesterol',views.cholest_viz),
    path('home/title/cartlist/results/energyviz/satunsat/cholesterol/cartotal',views.cart_viz),
    path('home/title/cartlist/results/energyviz/satunsat/cholesterol/cartotal/cartsum',views.cart_summary)


]