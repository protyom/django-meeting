from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from . import models
from allauth.utils import email_address_exists
from allauth.account.adapter import get_adapter
from allauth.account import app_settings as allauth_settings
from allauth.account.utils import setup_user_email
from django_countries.serializers import CountryFieldMixin


class UserSerializer(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('email', 'username', 'role', 'country', 'pk')
        extra_kwargs = {'password': {'write_only': True}}


class RegisterSerializerCustom(RegisterSerializer):
    STUDENT = "STD"
    TEACHER = "TCH"
    ROLES = (
        (STUDENT, "Student"),
        (TEACHER, "Teacher"),
    )
    role = serializers.ChoiceField(choices=ROLES, default="STD")

    def get_cleaned_data(self):
        return {
                'username': self.validated_data.get('username', ''),
                'password1': self.validated_data.get('password1', ''),
                'email': self.validated_data.get('email', ''),
                'role': self.validated_data.get('role', ''),
            }

    def validate_role(self, role):
        return role

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    _("A user is already registered with this e-mail address."))
        return email

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        user.role = self.cleaned_data.get('role')
        user.save()
        return user


class UserEditSerializer(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('first_name', 'last_name', 'country')
