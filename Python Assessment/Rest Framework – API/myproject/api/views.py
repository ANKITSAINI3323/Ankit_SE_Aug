from django.shortcuts import render
from.serializers import*
from.models import*
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import HttpResponse

# Create your views here.
def home(request):
    pass

@api_view(['GET'])
def getdata(request):
    if request.method == "GET":
        uall = student.objects.all()
        s_data = user_serializers(uall,many=True)
        return Response(s_data.data,status = status.HTTP_202_ACCEPTED)
    return Response(status=status.status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def insertdata(request,format = None):
    if request.method == "POST":
        data = request.data
        newuser = user_serializers(data=data)
        if newuser.is_valid():
            newuser.save()
            res = {"msg":"data been created succesfullyy"}
            return Response(sstatus=status.HTTP_201_CREATED)
        else:
            
            return Response( status=status.HTTP_400_BAD_REQUEST)