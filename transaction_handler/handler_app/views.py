# views.py (de la instancia de recepción)
import requests
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class TransaccionView(APIView):
    def post(self, request):
        # Obtener los datos de la transacción desde la solicitud
        transaccion_data = request.data

        # Enviar la transacción al balanceador de carga
        balanceador_url = 'http://10.128.0.5/'  # Cambiar a la URL del balanceador de carga

        # Enviar la transacción al balanceador de carga
        response = requests.post(balanceador_url, json=transaccion_data)

        # Verificar si la solicitud fue exitosa
        if response.status_code == 200 or response.status_code == 201:
            return Response({'status': 'Transacción enviada correctamente'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Error en el procesamiento'}, status=response.status_code)
