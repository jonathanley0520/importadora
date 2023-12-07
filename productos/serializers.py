from rest_framework import serializers
from .models import Producto, LoteImportacion, DetalleLote, Usuario, Compra

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class LoteImportacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoteImportacion
        fields = '__all__'

class DetalleLoteSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer()
    lote_importacion = LoteImportacionSerializer()

    class Meta:
        model = DetalleLote
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class CompraSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()
    detalle_lote = DetalleLoteSerializer()

    class Meta:
        model = Compra
        fields = '__all__'


