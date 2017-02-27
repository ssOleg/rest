from rest_framework import generics
from django.shortcuts import get_object_or_404

# # Create your views here.

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status


from . import models
from . import serializers


class ListCreateModule(generics.ListCreateAPIView):
    queryset = models.Module.objects.all()
    serializer_class = serializers.ModuleSerializer


class RetrieveUpdateDestroyModule(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Module.objects.all()
    serializer_class = serializers.ModuleSerializer


class ListCreateReview(generics.ListCreateAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

    def get_queryset(self):
        return self.queryset.filter(obj_id=self.kwargs.get('module_pk'))

    def perform_create(self, serializer):
        module = get_object_or_404(
            models.Module, pk=self.kwargs.get('module_pk')
        )
        serializer.save(obj=module)


class RetrieveUpdateDestroyReview(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

    def get_object(self):
        return get_object_or_404(
            self.get_queryset(),
            obj_id=self.kwargs.get('module_pk'),
            pk=self.kwargs.get('pk')
        )


# class AllModules(APIView):
#     """docstring for ClassName."""

#     def get(self, request, format=None):
#         """Docstring for MethodName."""
#         module = models.Module.objects.all()
#         serializer = serializers.ModuleSerializer(module, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         """Docstring for MethodName."""
#         serializer = serializers.ModuleSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
