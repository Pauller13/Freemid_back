# filters/name_concat_search_filter.py
from django.db import models
from rest_framework.filters import SearchFilter
from django.db.models import Value
from django.db.models.functions import Concat


class NameConcatSearchFilter(SearchFilter):
    def filter_queryset(self, request, queryset, view):
        search_terms = self.get_search_terms(request)
        if search_terms:
            # Concatenate first_name and last_name for both client and freelancer
            queryset = queryset.annotate(
                client_full_name=Concat('client__user__first_name', Value(' '), 'client__user__last_name'),
                freelancer_full_name=Concat('freelancer__user__first_name', Value(' '), 'freelancer__user__last_name'),
            )
            # Filter by client_full_name or freelancer_full_name, or individually by first_name or last_name
            queryset = queryset.filter(
                models.Q(client_full_name__icontains=search_terms[0]) |
                models.Q(freelancer_full_name__icontains=search_terms[0]) |
                models.Q(client__user__first_name__icontains=search_terms[0]) |
                models.Q(client__user__last_name__icontains=search_terms[0]) |
                models.Q(freelancer__user__first_name__icontains=search_terms[0]) |
                models.Q(freelancer__user__last_name__icontains=search_terms[0])
            )
        return queryset
