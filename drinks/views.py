from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Décorator Django -> utilisé pour indiquer quelles méthodes HTTP sont autorisées pour cette vue
@api_view(['GET', 'POST'])
def drink_list(request, format=None):

    if request.method == 'GET':
        # Obtenez toutes les boissons
        drinks = Drink.objects.all()
        # Sérialisez-les
        serializer = DrinkSerializer(drinks, many=True)
        # retour en json de toutes les boissons encapsuler dans drinks
        return Response({"drinks": serializer.data})

    elif request.method == 'POST':
        # Sérialise les données reçues dans la requête HTTP.
        serializer = DrinkSerializer(data=request.data)

        if serializer.is_valid():
            # Sauvegarder les données dans la base de données
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id, format=None):

    # Essaye d'obtenir l'object avec l'id
    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    