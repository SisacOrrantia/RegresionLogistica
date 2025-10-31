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
        x_value = serializer.validated_data['x']
        
        try:
            model_path = os.path.join(os.path.dirname(__file__), 'modelo_lineal.pkl')
            model = joblib.load(model_path)
            
            x_array = np.array([[x_value]])
            prediction = model.predict(x_array)[0]
            
            return Response({
                'prediction': float(prediction),
                'input': x_value
            })
        except Exception as e:
            return Response({
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
