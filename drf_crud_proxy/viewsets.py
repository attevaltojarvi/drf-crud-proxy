from rest_framework import viewsets

from drf_crud_proxy.mixins import ProxiedCreateModelMixin, ProxiedUpdateModelMixin, ProxiedListModelMixin, \
    ProxiedRetrieveModelMixin
from drf_crud_proxy.proxy import CRUDProxy


class ProxiedGenericViewSet(CRUDProxy, viewsets.GenericViewSet):
    pass


class ProxiedModelViewSet(
    CRUDProxy, ProxiedListModelMixin, ProxiedRetrieveModelMixin, ProxiedUpdateModelMixin, ProxiedCreateModelMixin,
    viewsets.ModelViewSet
):
    pass


class ProxiedReadOnlyModelViewSet(
    CRUDProxy, ProxiedListModelMixin, ProxiedRetrieveModelMixin, viewsets.ReadOnlyModelViewSet
):
    pass
