import django_filters as filters

from Things.models import Thing


class ThingListFilter(filters.FilterSet):
    class Meta:
        model = Thing
        fields = {
            "name": ["icontains"],
            "rank": ["icontains"],
            "suit": ["icontains"],
        }
