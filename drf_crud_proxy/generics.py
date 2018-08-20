from rest_framework import generics

from drf_crud_proxy.mixins import ProxiedCreateModelMixin, ProxiedUpdateModelMixin, ProxiedListModelMixin, \
    ProxiedRetrieveModelMixin
from drf_crud_proxy.proxy import CRUDProxy


class ProxiedCreateAPIView(CRUDProxy, ProxiedCreateModelMixin, generics.CreateAPIView):
    pass


class ProxiedUpdateAPIView(CRUDProxy, ProxiedUpdateModelMixin, generics.UpdateAPIView):
    pass


class ProxiedListAPIView(CRUDProxy, ProxiedListModelMixin, generics.ListAPIView):
    pass


class ProxiedRetrieveAPIView(CRUDProxy, ProxiedRetrieveModelMixin, generics.RetrieveAPIView):
    pass


class ProxiedListCreateAPIView(CRUDProxy, ProxiedCreateModelMixin, ProxiedListModelMixin, generics.ListCreateAPIView):
    pass


class ProxiedRetrieveDestroyAPIView(CRUDProxy, ProxiedRetrieveModelMixin, generics.RetrieveDestroyAPIView):
    pass


class ProxiedRetrieveUpdateAPIView(
    CRUDProxy, ProxiedUpdateModelMixin, ProxiedRetrieveModelMixin, generics.RetrieveUpdateAPIView
):
    pass


class ProxiedRetrieveUpdateDestroyAPIView(
    CRUDProxy, ProxiedUpdateModelMixin, ProxiedRetrieveModelMixin, generics.RetrieveUpdateDestroyAPIView
):
    pass
