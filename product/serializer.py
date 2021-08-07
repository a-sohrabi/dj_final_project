from rest_framework import serializers


from .models import Category, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = '__all__'
        fields = [
            'id',
            'name',
            'get_absolute_url',
            'description',
            'price',
            'get_image',
            'get_thumbnail',
        ]

# class productserialzer1(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = '__all__'
