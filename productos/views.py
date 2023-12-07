# productos/views.py
from rest_framework import generics
from .models import Producto, LoteImportacion, DetalleLote, Usuario, Compra
from .serializers import ProductoSerializer, LoteImportacionSerializer, DetalleLoteSerializer, UsuarioSerializer, CompraSerializer

class ProductoListCreateView(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class LoteImportacionListCreateView(generics.ListCreateAPIView):
    queryset = LoteImportacion.objects.all()
    serializer_class = LoteImportacionSerializer

class LoteImportacionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LoteImportacion.objects.all()
    serializer_class = LoteImportacionSerializer

class DetalleLoteListCreateView(generics.ListCreateAPIView):
    queryset = DetalleLote.objects.all()
    serializer_class = DetalleLoteSerializer

class DetalleLoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DetalleLote.objects.all()
    serializer_class = DetalleLoteSerializer

class UsuarioListCreateView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class CompraListCreateView(generics.ListCreateAPIView):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer

class CompraDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer



