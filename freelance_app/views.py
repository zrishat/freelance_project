from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions, viewsets

from freelance_app.models import Executor, Customer, Task, Message, Support
from freelance_app.serializers import CustomerSerializer, ExecutorSerializer, SupportSerializer, MessageSerializer, \
    TaskSerializer


# class ExecutorListView(generics.ListAPIView):
#     queryset = Executor.objects.all()
#     serializer_class = ExecutorSerializer
#
#
# class CustomerListView(generics.ListAPIView):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer

class SupportViewSet(viewsets.ModelViewSet):
    """
    API
    """
    queryset = Support.objects.all()
    serializer_class = SupportSerializer
    permission_classes = [permissions.IsAuthenticated]


class MessageViewSet(viewsets.ModelViewSet):
    """
    API
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]


class TaskViewSet(viewsets.ModelViewSet):
    """
    API
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    """
    API
    """
    queryset = User.objects.all()
    serializer_class = ExecutorSerializer
    permission_classes = [permissions.IsAuthenticated]


class ExecutorViewSet(viewsets.ModelViewSet):
    """
    API
    """
    queryset = Executor.objects.all()
    serializer_class = ExecutorSerializer
    permission_classes = [permissions.IsAuthenticated]


class CustomerViewSet(viewsets.ModelViewSet):
    """
    API
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]
