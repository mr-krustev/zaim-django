from django.urls import path

from . import views

app_name = 'products'
urlpatterns = [
    path('', views.ProductsListView.as_view(), name='index'),
    path('<pk>/', views.ProductDetailView.as_view(), name='detail')
]
