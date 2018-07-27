from django.urls import path
from . import views


urlpatterns = [
    path('product/list/', views.show_product_page),
]