from rest_framework import serializers
from .models import Hall

class HallSerizlizer(serializers.ModelSerializer):

    class Meta:
        model = Hall
        fields = ("id","name","seats",
                  "description",
                  "available_equipment",
                  )