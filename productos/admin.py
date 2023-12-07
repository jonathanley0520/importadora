from django.contrib import admin
from .models import Producto, LoteImportacion, DetalleLote, Usuario, Compra


admin.site.register(Producto)
admin.site.register(LoteImportacion)
admin.site.register(DetalleLote)
admin.site.register(Usuario)
admin.site.register(Compra)

