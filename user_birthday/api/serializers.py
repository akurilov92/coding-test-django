from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    birthday = serializers.DateField(format="%d.%m.%Y", input_formats=["%d.%m.%Y"])

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "birthday")
