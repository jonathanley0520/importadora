from django.db import models

class Producto(models.Model):
    
    nombre = models.CharField(max_length=255)
    peso = models.FloatField()
    volumen = models.FloatField()
    unidades_disponibles = models.IntegerField(default=0)
    
    def __str__(self):
        return self.nombre 

class LoteImportacion(models.Model):
    
    costo_importacion_metro_cubico = models.FloatField(default=1850000.00)
    arancel = models.FloatField(default=6.0)
    costo_flete_interno_tonelada = models.FloatField(default=600000.00)
    impuesto_iva = models.FloatField(default=19.0)

class DetalleLote(models.Model):
    
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    lote_importacion = models.ForeignKey(LoteImportacion, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)
    
class Usuario(models.Model):
    
    correo = models.EmailField(unique=True)
    confirmado = models.BooleanField(default=False)
    
class Compra(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    detalle_lote = models.ForeignKey(DetalleLote, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)
    precio_venta = models.FloatField(default=0.0)
    descuento_por_cantidad = models.FloatField(default=0.0)
    

    

