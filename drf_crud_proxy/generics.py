from rest_framework import generics

from drf_crud_proxy.mixins import CreateModelMixin, UpdateModelMixin, ListModelMixin, RetrieveModelMixin
from drf_crud_proxy.proxy import CRUDProxy


class CreateAPIView(CRUDProxy, CreateModelMixin, generics.CreateAPIView):
    pass


class UpdateAPIView(CRUDProxy, UpdateModelMixin, generics.UpdateAPIView):
    pass


class ListAPIView(CRUDProxy, ListModelMixin, generics.ListAPIView):
    pass


class RetrieveAPIView(CRUDProxy, RetrieveModelMixin, generics.RetrieveAPIView):
    pass


class ListCreateAPIView(CRUDProxy, CreateModelMixin, ListModelMixin, generics.ListCreateAPIView):
    pass


class RetrieveDestroyAPIView(CRUDProxy, RetrieveModelMixin, generics.RetrieveDestroyAPIView):
    pass


class RetrieveUpdateAPIView(CRUDProxy, UpdateModelMixin, RetrieveModelMixin, generics.RetrieveUpdateAPIView):
    pass


class RetrieveUpdateDestroyAPIView(CRUDProxy, UpdateModelMixin, RetrieveModelMixin, generics.RetrieveUpdateDestroyAPIView):
    pass
