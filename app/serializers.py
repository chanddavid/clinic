from rest_framework import serializers
from .models import User,Role,StaffRole


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            "salt": {'read_only': True},
            "hashed_password": {'read_only': True},
            "last_login": {'read_only': True}
        }

class RoleSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        style={'placeholder': 'Name'}
    )
    class Meta:
        model = Role
        fields = "__all__"


class StaffRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffRole
        fields = "__all__"
