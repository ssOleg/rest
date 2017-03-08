from rest_framework import generics, viewsets, mixins
from django.shortcuts import get_object_or_404
from rest_framework.decorators import detail_route

# # Create your views here.

# from rest_framework.views import APIView
from rest_framework.response import Response
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


class ModuleViewSet(viewsets.ModelViewSet):
    queryset = models.Module.objects.all()
    serializer_class = serializers.ModuleSerializer

    @detail_route(methods=['GET', ])
    def reviews(self, request, pk=None):
        # modul = self.get_object()
        # serializer = serializers.ReviewSerializer(
        #     modul.reviews.all(),
        #     many=True
        # )
        # return Response(serializer.data)
        self.pagination_class.page_size = 1
        reviews = models.Review.objects.filter(obj_id=pk)
        page = self.paginate_queryset(reviews)

        if page is not None:
            serializer = serializers.ReviewSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = serializers.ReviewSerializer(
            reviews, many=True
        )
        return Response(serializer.data)


class ReviewViewSet(
    # mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    # class ReviewViewSet(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer


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
