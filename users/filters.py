from django_filters import rest_framework as rest_filters, CharFilter

from users.models import User

class UserFilter(rest_filters.FilterSet):
    username = CharFilter(field_name='username', lookup_expr='icontains')

    class Meta:
        model = User
        fields = ['username', 'email']