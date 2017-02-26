from rest_framework import serializers
from . import models


class ReviewSerializer(serializers.ModelSerializer):
    """docstring for ClassName."""

    class Meta:
        """docstring for ClassName."""

        model = models.Review
        fields = (
            'id', 'obj', 'email', 'name', 'comment', 'time_creation'
        )
        extra_quargs = {
            'email': {'write_only': True}
        }


class ModuleSerializer(serializers.ModelSerializer):
    """docstring for ClassName."""

    class Meta:
        """docstring for ClassName."""

        model = models.Module
        fields = (
            'id', 'name', 'url'
        )