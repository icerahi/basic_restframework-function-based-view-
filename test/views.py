from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from test.models import Contact
from test.serializers import ContactSerializer

@api_view(['GET','POST'])
def contact_list(request):
    if request.method=="GET":
        obj=Contact.objects.all()
        serializer=ContactSerializer(obj,many=True)
        return Response(serializer.data)

    elif request.method=="POST":
        serializer=ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
def contact_details(request,pk):
    try:
        obj=Contact.objects.get(pk=pk)
    except Contact.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=="GET":
        serializer=ContactSerializer(obj)
        return Response(serializer.data)

    elif request.method=="PUT":
        serializer=ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


