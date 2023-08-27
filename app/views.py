from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Customer, Product, People
from rest_framework.views import APIView
from .serializers import SerializedCustomer, SerializedProduct, SerializedPeople


class Customer_view(APIView):

    def get(self, req):
        customers = Customer.objects.all()
        serialized_customers = SerializedCustomer(customers, many=True)
        data = serialized_customers.data
        return Response(data, status=status.HTTP_200_OK)


class Product_view(APIView):

    def get(self, req):
        price = req.query_params.get('price')
        price_2 = req.query_params.get('price')
        title = req.query_params.get('title')
        products = Product.objects.all()
        if title:
            products = Product.objects.filter(title__title=title)
        if price:
            products = Product.objects.filter(price__lte=price)
        if price_2:
            products = Product.objects.filter(price_2__gte=price_2)
        serialized_products = SerializedProduct(products, many=True)
        data = serialized_products.data
        return Response(data, status=status.HTTP_200_OK)

class People_view(APIView):

    def get(self, req):
        category = req.query_params.get('category')
        people = People.objects.all()
        if category:
            people = People.objects.filter(category__title=category)
        serialized_people = SerializedPeople(people, many=True)
        data = serialized_people.data
        return Response(data, status=status.HTTP_200_OK)