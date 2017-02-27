from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from . import models
from . import serializers


class AllModules(APIView):
    """docstring for ClassName."""

    def get(self, request, format=None):
        """Docstring for MethodName."""
        module = models.Module.objects.all()
        serializer = serializers.ModuleSerializer(module, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """Docstring for MethodName."""
        serializer = serializers.ModuleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
