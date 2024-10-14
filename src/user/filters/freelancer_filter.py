from django_filters import rest_framework as filters
from user.models.freelancer_model import FreelancerModel
from django.db import models


class FreelancerFilter(filters.FilterSet):
    class Meta:
        model = FreelancerModel
        fields = ['skills']
        filter_overrides = {
            models.JSONField: {
                'filter_class': filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',  # ou 'exact', selon vos besoins
                },
            },
        }
