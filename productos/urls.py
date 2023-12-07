from django.urls import path , include
from .views import (
    ProductoListCreateView, ProductoDetailView,
    LoteImportacionListCreateView, LoteImportacionDetailView,
    DetalleLoteListCreateView, DetalleLoteDetailView,
    UsuarioListCreateView, UsuarioDetailView,
    CompraListCreateView, CompraDetailView
)

urlpatterns = [
    path('productos/', ProductoListCreateView.as_view(), name='producto-list-create'),
    path('productos/<int:pk>/', ProductoDetailView.as_view(), name='producto-detail'),

    path('lotes/', LoteImportacionListCreateView.as_view(), name='lote-list-create'),
    path('lotes/<int:pk>/', LoteImportacionDetailView.as_view(), name='lote-detail'),

    path('detalles/', DetalleLoteListCreateView.as_view(), name='detalle-list-create'),
    path('detalles/<int:pk>/', DetalleLoteDetailView.as_view(), name='detalle-detail'),

    path('usuarios/', UsuarioListCreateView.as_view(), name='usuario-list-create'),
    path('usuarios/<int:pk>/', UsuarioDetailView.as_view(), name='usuario-detail'),

    path('compras/', CompraListCreateView.as_view(), name='compra-list-create'),
    path('compras/<int:pk>/', CompraDetailView.as_view(), name='compra-detail'),
]
