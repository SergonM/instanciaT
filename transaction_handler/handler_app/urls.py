# urls.py (en la instancia de recepción)
from django.urls import path
from .views import TransaccionView

urlpatterns = [
    path('transaccion/', TransaccionView.as_view(), name='transaccion'),
]
