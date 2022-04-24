from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class ExecutorSerializer(serializers.ModelSerializer):
    # user = UserSerializer()

    class Meta:
        model = Executor
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    # user = UserSerializer()

    class Meta:
        model = Customer
        fields = '__all__'


class SupportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Support
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'
        extra_kwargs = {"executor": {"required": False, "allow_null": True}}