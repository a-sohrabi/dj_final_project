from django.urls import path, include

from product import views

urlpatterns = [
    path('latestproducts/', views.LatestProductLists.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view())

]