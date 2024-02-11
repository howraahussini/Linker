from django_filters import rest_framework as filters
from ...models import MainLink


class MainLinkFilter(filters.FilterSet):
    '''
    this is for filter MainLink by author.
    '''
    
    class Meta:
        model = MainLink
        fields = {
            "author": [
                "exact",
            ],
        }