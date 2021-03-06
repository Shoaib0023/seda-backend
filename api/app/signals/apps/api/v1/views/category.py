from datapunt_api.pagination import HALPagination
from datapunt_api.rest import DatapuntViewSet
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from signals.apps.api.generics.mixins import RetrieveModelMixin, UpdateModelMixin
from signals.apps.api.generics.permissions import ModelWritePermissions, SIAPermissions
from signals.apps.api.v1.serializers import (
    CategoryHALSerializer,
    ParentCategoryHALSerializer,
    PrivateCategorySerializer
)
from signals.apps.api.v1.serializers.category import PrivateCategoryHistoryHalSerializer
from signals.apps.signals.models import Category
from signals.auth.backend import JWTAuthBackend


class ParentCategoryViewSet(DatapuntViewSet):
    queryset = Category.objects.filter(parent__isnull=True)
    serializer_detail_class = ParentCategoryHALSerializer
    serializer_class = ParentCategoryHALSerializer
    # lookup_field = 'slug'
    lookup_fields = (('category_level_name1'), ('category_level_name2'), ('category_level_name3'), ('category_level_name4'))


class CategoryNameViewSet(RetrieveModelMixin, GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryHALSerializer
    pagination_class = HALPagination

    def get_object(self):
        # print(self.kwargs)
        queryset = self.filter_queryset(self.get_queryset())

        if 'cat4' in self.kwargs:
            obj = get_object_or_404(queryset,
                                    category_level_name1=self.kwargs['cat1'],
                                    category_level_name2=self.kwargs['cat2'],
                                    category_level_name3=self.kwargs['cat3'],
                                    category_level_name4=self.kwargs['cat4'])
        else:
            obj = get_object_or_404(queryset,
                                    category_level_name1=self.kwargs['cat1'],
                                    category_level_name2=self.kwargs['cat2'],
                                    category_level_name3=self.kwargs['cat3'])

        self.check_object_permissions(self.request, obj)
        return obj


# to be removed
class ChildCategoryViewSet(RetrieveModelMixin, GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryHALSerializer
    pagination_class = HALPagination

    def get_object(self):
        # print(self.kwargs)
        queryset = self.filter_queryset(self.get_queryset())

        if 'slug' in self.kwargs and 'sub_slug' in self.kwargs:
            obj = get_object_or_404(queryset,
                                    parent__slug=self.kwargs['slug'],
                                    slug=self.kwargs['sub_slug'])
        else:
            obj = get_object_or_404(queryset, slug=self.kwargs['slug'])

        self.check_object_permissions(self.request, obj)
        return obj


class PrivateCategoryViewSet(UpdateModelMixin, DatapuntViewSet):
    serializer_class = PrivateCategorySerializer
    serializer_detail_class = PrivateCategorySerializer

    queryset = Category.objects.all()

    authentication_classes = (JWTAuthBackend,)
    permission_classes = (SIAPermissions & ModelWritePermissions,)

    @action(detail=True)
    def history(self, request, pk=None):
        """
        The change log of the selected Category instance
        This is read-only!
        """
        category = self.get_object()
        serializer = PrivateCategoryHistoryHalSerializer(category.logs, many=True)
        return Response(serializer.data)
