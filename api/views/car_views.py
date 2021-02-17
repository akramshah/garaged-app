from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.car import Car
from ..serializers import CarSerializer, UserSerializer

class Cars(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = CarSerializer
    def get(self, request):
        """Index request"""
        cars = Car.objects.filter(owner=request.user.id)
        data = CarSerializer(cars, many=True).data
        return Response({ 'cars': data })

    def post(self, request):
        """Create request"""
        request.data['car']['owner'] = request.user.id
        car = CarSerializer(data=request.data['car'])
        if car.is_valid():
            car.save()
            return Response({ 'car': car.data }, status=status.HTTP_201_CREATED)
        return Response(car.errors, status=status.HTTP_400_BAD_REQUEST)

class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        car = get_object_or_404(Car, pk=pk)
        if not request.user.id == car.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this car')
        data = CarSerializer(car).data
        return Response({ 'car': data })

    def delete(self, request, pk):
        """Delete request"""
        car = get_object_or_404(Car, pk=pk)
        if not request.user.id == car.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this car')
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        if request.data['car'].get('owner', False):
            del request.data['car']['owner']

        car = get_object_or_404(Car, pk=pk)
        if not request.user.id == car.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this car')

        request.data['car']['owner'] = request.user.id
        data = CarSerializer(car, data=request.data['car'])
        if data.is_valid():
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
