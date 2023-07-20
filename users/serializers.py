from rest_framework import serializers
from users.models import User

from django.contrib.auth import get_user_model, authenticate
from djoser.conf import settings
from djoser.serializers import TokenCreateSerializer

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "UsersUserSerializer"
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        password = validated_data['password']
        user.set_password(password)  # Захешировать пароль
        user.save()
        return user


class CustomTokenCreateSerializer(TokenCreateSerializer):

    def validate(self, attrs):
        password = attrs.get("password")
        params = {settings.LOGIN_FIELD: attrs.get(settings.LOGIN_FIELD)}
        self.user = authenticate(
            request=self.context.get("request"), **params, password=password
        )
        if not self.user:
            self.user = User.objects.filter(**params).first()
            if self.user and not self.user.check_password(password):
                self.fail("invalid_credentials")
        if self.user: # and self.user.is_active:
            return attrs
        self.fail("invalid_credentials")

