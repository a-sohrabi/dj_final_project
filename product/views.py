from django.db.models import Q
from django.http import Http404, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from .models import Product, Category
from .serializer import ProductSerializer, CategorySerializer


class LatestProductsList(APIView):

    def get(self, request, format=None):
        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Product.DoesNotExist:
            raise Http404


    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug,)
        serializer = CategorySerializer(category)
        return Response(serializer.data)


@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({'products': []})

# def product_api(request):
#     if request.method == 'GET':
#         products = Product.objects.all()
#         serial = ProductSerializer(products, many=True)
#         return JsonResponse({
#             'products': serial.data
#         })
#     elif request.method == 'POST':
#         serial = ProductSerializer(data=request.POST)
#         if serial.is_valid():
#             serial.save()
#             return JsonResponse(serial.data)
#         else:
#             return JsonResponse(serial.errors, status=400)


from rest_framework import generics


# class ProductListApiView(generics.ListCreateAPIView):
#     serializer_class = ProductSerializer
#     queryset = Product.objects.all()

    # def get_serializer(self, *args, **kwargs):
    #     if self.request.method == "POST":
    #         return productserialzer1
    #     return super().get_serializer(*args, **kwargs)

#
# class ProductDetailApi(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = ProductSerializer
#     queryset = Product.objects.all()

