from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import status
from rest_framework import permissions
from ShopApp.models import Category, Product, Choice
from .serializers import CategorySerializer, ProductSerializer, ChoiceSerializer 
from rest_framework import viewsets


# Create your views here.

class CategoryListAPIView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    #def get(self, request, *args, **kwargs):
    #    category = Category.objects
    #    serializer = CategorySerializer(category, many=True)
    #    return Response(serializer.data, status=status.HTTP_200_OK)


class ProductListAPIView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # def get(self, request, *args, **kwargs):
    #     product = Product.objects
    #     serializer = ProductSerializer(product, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)


class ChoiceListAPIView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class SingleCategoryRetrieveAPIView(RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SingleProductRetrieveAPIView(RetrieveAPIView):
    permission_class = [permissions.IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class SingleChoiceRetrieveAPIView(RetrieveAPIView):
    permission_class = [permissions.IsAuthenticated]
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer 


class CreateCategoryAPIView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # def create_category(self, serializer):
    #     category = get_object_or_404(Category, id=self.request.data.get('category_id'))
    #     return serializer.save(category=category)


class CreateProductAPIView(CreateAPIView):
    permission_class = [permissions.IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CreateChoiceAPIView(CreateAPIView):
    permission_class = [permissions.IsAuthenticated]
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class CategoryUpdateAPIView(UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductUpdateAPIView(UpdateAPIView):
    permission_class = [permissions.IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ChoiceUpdateAPIView(UpdateAPIView):
    permission_class = [permissions.IsAuthenticated]
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class DeleteCategoryAPIView(DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DeleteProductAPIView(DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class DeleteChoiceAPIView(DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer