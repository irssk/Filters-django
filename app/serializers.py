from rest_framework import serializers
from rest_framework.serializers import IntegerField, SerializerMethodField
from app import models


class SerializedCategory(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['title', 'description']

class SerializedCustomer(serializers.ModelSerializer):
    actual_age = IntegerField(source = 'age')
    new_double_age = SerializerMethodField(method_name='double_age')
    category = SerializedCategory(read_only=True)
    category_id = IntegerField(write_only=True)

    class Meta:
        model = models.Customer
        fields = ['name', 'surname', 'image', 'age', 'cart', 'category', 'category_id']


class SerializedCart(serializers.ModelSerializer):
    class Meta:
        model = models.Cart
        fields = '__all__'

class SerializedDelivery_Crew(serializers.ModelSerializer):
    class Meta:
        model = models.Delivery_Crew
        fields = '__all__'

class SerializedProduct(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'

class SerializedManager(serializers.ModelSerializer):
    class Meta:
        model = models.Manager
        fields = '__all__'

class SerializedPeople(serializers.ModelSerializer):
    class Meta:
        model = models.People
        fields = '__all__'