from rest_framework import viewsets

from drf_crud_proxy.mixins import CreateModelMixin, UpdateModelMixin, ListModelMixin, RetrieveModelMixin
from drf_crud_proxy.proxy import CRUDProxy


class GenericViewSet(CRUDProxy, viewsets.GenericViewSet):
    pass


class ModelViewSet(CRUDProxy, CreateModelMixin, UpdateModelMixin, ListModelMixin, RetrieveModelMixin, viewsets.ModelViewSet):
    pass


class ReadOnlyModelViewSet(CRUDProxy, ListModelMixin, RetrieveModelMixin, viewsets.ReadOnlyModelViewSet):
    pass
