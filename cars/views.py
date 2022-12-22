# Create your views here.
# Where we define all the functions the outside world can interact with through urls over the internet.
# Decorator is going to assign certian permissions to that function.
# Here we will define what request types that function is capable of handling.
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CarSerializer
from .models import Car

@api_view(['GET', 'POST'])
def cars_list(request):

    if request.method == "GET":
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = CarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(["GET", "PUT", "DELETE"])
def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == "GET":
        serializer = CarSerializer(car)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = CarSerializer(car, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
