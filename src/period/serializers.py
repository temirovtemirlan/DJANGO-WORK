from rest_framework import serializers
from .models import Sessions

class SessionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sessions
        fields = ('movie','hall','start_time','end_time','available_seats')
