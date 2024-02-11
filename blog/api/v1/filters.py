from django_filters import rest_framework as filters

from ...models import Comment, Post


class PostFilter(filters.FilterSet):
    """
    class post filter is for filter posts with categories, author and status.
    """

    class Meta:
        model = Post
        fields = {
            "author": [
                "exact",
            ],
            "category": [
                "exact",
            ],
        }
        
class CommentFilter(filters.FilterSet):
    '''
    class comment filter is for filter comments by post_id.
    '''
    
    class Meta:
        model = Comment
        fields = {
            'post': [
                'exact',
            ],
        }