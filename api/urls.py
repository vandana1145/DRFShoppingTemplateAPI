from django.conf.urls import url
from django.urls import path, include
from .views import (
    CategoryListAPIView,
    SingleCategoryRetrieveAPIView,
    CreateCategoryAPIView,
    CategoryUpdateAPIView,
    DeleteCategoryAPIView,
    ProductListAPIView,
    SingleProductRetrieveAPIView,
    CreateProductAPIView,
    ProductUpdateAPIView,
    DeleteProductAPIView,
    ChoiceListAPIView,
    SingleChoiceRetrieveAPIView,
    CreateChoiceAPIView,
    ChoiceUpdateAPIView,
    DeleteChoiceAPIView
)

urlpatterns = [
    path('categories', CategoryListAPIView.as_view()),
    path('category/<int:pk>/', SingleCategoryRetrieveAPIView.as_view()),
    path('category/create/', CreateCategoryAPIView.as_view()),
    path('category/update/<int:pk>/', CategoryUpdateAPIView.as_view()),
    path('category/delete/<int:pk>/', DeleteCategoryAPIView.as_view()),
    path('products', ProductListAPIView.as_view()),
    path('product/<int:pk>/', SingleProductRetrieveAPIView.as_view()),
    path('product/create', CreateProductAPIView.as_view()),
    path('product/update/<int:pk>/', ProductUpdateAPIView.as_view()),
    path('product/delete/<int:pk>/', DeleteProductAPIView.as_view()),
    path('choices', ChoiceListAPIView.as_view()),
    path('choice/<int:pk>/', SingleChoiceRetrieveAPIView.as_view()),
    path('choice/create', CreateChoiceAPIView.as_view()),
    path('choice/update/<int:pk>/', ChoiceUpdateAPIView.as_view()),
    path('choice/delete/<int:pk>/', DeleteChoiceAPIView.as_view())
]
