from django.urls import path

from . import views

urlpatterns = [
    #path('customers/', views.Customer_view.as_view()),
    #path('customers/<int:customer_id>', views.Customer_view.as_view()),
    path('products/', views.Product_view.as_view()),
    path('products/<int:product_id>', views.Product_view.as_view()),
    path('people/', views.People_view.as_view()),
    path('people/<int:people_id>', views.People_view.as_view()),
    ]