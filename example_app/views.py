from rest_framework.generics import GenericAPIView

from drf_crud_proxy import generics, viewsets, mixins
from drf_crud_proxy.proxy import CRUDProxy
from .models import Order
from .serializers import OrderCreateSerializer, OrderListSerializer


class OrderBaseEndpoint(object):
    queryset = Order.objects.all()
    request_serializer_class = OrderCreateSerializer
    response_serializer_class = OrderListSerializer


class OrderListCreateEndpoint(OrderBaseEndpoint, generics.ProxiedListCreateAPIView):
    pass


class OrderListWithoutReadSerializerEndpoint(generics.ProxiedListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer


class OrderRetrieveUpdateDestroyEndpoint(OrderBaseEndpoint, generics.ProxiedRetrieveUpdateDestroyAPIView):
    pass


class OrderRetrieveUpdateEndpoint(OrderBaseEndpoint, generics.ProxiedRetrieveUpdateAPIView):
    pass


class OrderCreateWithGenericEndpoint(OrderBaseEndpoint, generics.ProxiedCreateAPIView):
    pass


class OrderUpdateWithGenericEndpoint(OrderBaseEndpoint, generics.ProxiedUpdateAPIView):
    pass


class OrderListWithGenericEndpoint(OrderBaseEndpoint, generics.ProxiedListAPIView):
    pass


class OrderRetrieveWithGenericEndpoint(OrderBaseEndpoint, generics.ProxiedRetrieveAPIView):
    pass


class OrderCreateWithMixinEndpoint(CRUDProxy, OrderBaseEndpoint, GenericAPIView, mixins.ProxiedCreateModelMixin):
    pass

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class OrderUpdateWithMixinEndpoint(CRUDProxy, OrderBaseEndpoint, GenericAPIView, mixins.ProxiedUpdateModelMixin):
    pass

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class OrderListWithMixinEndpoint(CRUDProxy, OrderBaseEndpoint, GenericAPIView, mixins.ProxiedListModelMixin):
    pass

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class OrderRetrieveWithMixinEndpoint(CRUDProxy, OrderBaseEndpoint, GenericAPIView, mixins.ProxiedRetrieveModelMixin):
    pass

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class OrderViewset(OrderBaseEndpoint, viewsets.ProxiedModelViewSet):
    pass
