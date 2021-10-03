from django.urls import path
from . import views

urlpatterns = [
     path('', views.display_homepage, name='home'),
     path('store/', views.products, name='products'),
     path('<int:product_id>/', views.single_product, name='single_product'),
     path('search/', views.search_result, name='search_result'),
     path('store/add/', views.add_product, name='add_product'),
     path('store/update/<int:product_id>/',
          views.update_product, name='update_product'),
     path('store/delete_warning/<int:product_id>/',
          views.delete_warning, name='delete_warning'),
     path('store/delete_product/<int:product_id>/',
          views.delete_product, name='delete_product'),
     path('store/hidden_products/',
          views.hidden_products, name='hidden_products'),
     path('store/out_of_stock_products/',
          views.out_of_stock_products, name='out_of_stock_products'),
     path('store/best_sellers/',
          views.best_sellers, name='best_sellers'),
     ]
