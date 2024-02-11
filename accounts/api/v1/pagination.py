from rest_framework.pagination import PageNumberPagination


class Pagination(PageNumberPagination):
    """
    class Pagination is for
    """

    page_size = 6
    page_size_query_param = "page_size"
