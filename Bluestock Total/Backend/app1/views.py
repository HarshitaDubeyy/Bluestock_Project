from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets,status
from .models import Item
from .serializers import ItemSerializer
from django.views.decorators.csrf import csrf_exempt
import json
from django.views import View
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
def ok(request):
#   item = Item.objects.filter(name=val)
  return render(request,'index.html')

# class ItemViewSet(viewsets.ModelViewSet):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer




class DetailView(View):
    def get(self,request,val):
        print(val)
        product = Item.objects.get(box=val)
        return render(request,'Content.html',locals())
    
@api_view(['GET', 'POST', 'PUT'])
def ipo_list(request):
    if request.method == 'GET':
        ipo_list = Item.objects.all()
        serialized = ItemSerializer(ipo_list,many=True)
        return Response(serialized.data)
    elif request.method == 'POST':
        _data = request.data
        serialized = ItemSerializer(data = _data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status= status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        serializer = ItemSerializer(Item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
