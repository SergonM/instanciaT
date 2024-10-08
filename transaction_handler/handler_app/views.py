import requests
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class TransaccionView(APIView):
    def put(self, request):
        transaccion_data = request.data

        curso_id = transaccion_data.get('id')
        balanceador_url = f'http://10.128.0.5/{curso_id}/'
        response = requests.put(balanceador_url, json=transaccion_data)
        # Verificar si la solicitud fue exitosa
        if response.status_code == 200 or response.status_code == 201:
            return Response({'status': 'Transacción enviada correctamente'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Error en el procesamiento'}, status=response.status_code)