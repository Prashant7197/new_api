import uuid
from django.shortcuts import render
from .models import Company, News
from django.http import HttpResponse, JsonResponse
from new1 import serializers
from new1.models import News, Company
from new1.serializers import UserSerializer, GroupSerializer
from rest_framework import generics, permissions, status, serializers
from rest_framework.response import Response
from django.contrib.auth.models import User

class RegistrationAPIView(generics.GenericAPIView):
    serializer_class = UserSerializer
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        
        if(serializer.is_valid()):
            serializer.save()
            return Response({
                "RequestID": str(uuid.uuid4()),
                "Message": "User created successfully",
                "User": serializer.data}, status=status.HTTP_201_CREATED
                            )
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
class UserList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer