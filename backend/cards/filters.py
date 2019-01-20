from rest_framework.filters import BaseFilterBackend


class AuthorOrAdminFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if request.user.is_staff:
            return queryset
        return queryset.filter(author=request.user.account)
