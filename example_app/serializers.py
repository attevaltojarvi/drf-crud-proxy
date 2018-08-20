from rest_framework import serializers
from .models import Order, OrderedProduct, Product


class OrderedProductCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderedProduct
        fields = ('id', 'quantity', 'product')


class OrderCreateSerializer(serializers.ModelSerializer):
    ordered_products = OrderedProductCreateSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'customer', 'ordered_products', 'total_price')

    def create(self, validated_data):
        ordered_products_dict_list = validated_data.pop('ordered_products')
        instance = Order.objects.create(**validated_data)

        for ordered_product_dict in ordered_products_dict_list:
            instance.ordered_products.create(**ordered_product_dict)

        return instance

    def update(self, instance, validated_data):
        ordered_products_dict_list = validated_data.pop('ordered_products', None)

        instance.customer = validated_data.pop('customer', instance.customer)
        instance.save()

        if ordered_products_dict_list is not None:
            instance.ordered_products.all().delete()
            for ordered_product_dict in ordered_products_dict_list:
                instance.ordered_products.create(**ordered_product_dict)

        return instance


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price')


class OrderedProductDetailsSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderedProduct
        fields = ('id', 'quantity', 'product')


class OrderListSerializer(serializers.ModelSerializer):
    ordered_products = OrderedProductDetailsSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'customer', 'ordered_products', 'total_price')
