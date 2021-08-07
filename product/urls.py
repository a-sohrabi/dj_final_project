from django.urls import path, include

from .views import *


urlpatterns = [
    path('latest-products/', LatestProductsList.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/', ProductDetail.as_view()),
    # path('product_api/', ProductListApiView.as_view()),
    # path('product_detail_api/<int:pk>', ProductDetailApi.as_view())

]