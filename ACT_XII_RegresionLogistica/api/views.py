import numpy as np
import joblib
import os
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import PredictionSerializer

def index(request):
    return render(request, 'index.html')

@api_view(['POST'])
def predict(request):
    serializer = PredictionSerializer(data=request.data)
    
    if serializer.is_valid():
        edad = serializer.validated_data['edad']
        salario = serializer.validated_data['salario']
        
        try:
            model_path = os.path.join(os.path.dirname(__file__), 'modelo_regresion_logistica.pkl')
            scaler_path = os.path.join(os.path.dirname(__file__), 'scaler.pkl')
            
            model = joblib.load(model_path)
            scaler = joblib.load(scaler_path)
            
            datos = np.array([[edad, salario]])
            datos_escalados = scaler.transform(datos)
            
            prediccion = model.predict(datos_escalados)[0]
            probabilidad = model.predict_proba(datos_escalados)[0][1]
            
            resultado = "Comprara" if prediccion == 1 else "No comprara"
            
            return Response({
                'prediccion': resultado,
                'probabilidad': float(probabilidad),
                'edad': edad,
                'salario': salario
            })
        except Exception as e:
            return Response({
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
