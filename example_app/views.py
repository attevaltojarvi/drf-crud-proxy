from rest_framework.generics import GenericAPIView

from drf_crud_proxy import generics, viewsets, mixins
from drf_crud_proxy.proxy import CRUDProxy
from .models import Order
from .serializers import OrderCreateSerializer, OrderListSerializer


class OrderBaseEndpoint(object):
    queryset = Order.objects.all()
    request_serializer_class = OrderCreateSerializer
    response_serializer_class = OrderListSerializer


class OrderListCreateEndpoint(OrderBaseEndpoint, generics.ListCreateAPIView):
    pass


class OrderListWithoutReadSerializerEndpoint(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer


class OrderRetrieveUpdateDestroyEndpoint(OrderBaseEndpoint, generics.RetrieveUpdateDestroyAPIView):
    pass


class OrderRetrieveUpdateEndpoint(OrderBaseEndpoint, generics.RetrieveUpdateAPIView):
    pass


class OrderCreateWithGenericEndpoint(OrderBaseEndpoint, generics.CreateAPIView):
    pass


class OrderUpdateWithGenericEndpoint(OrderBaseEndpoint, generics.UpdateAPIView):
    pass


class OrderListWithGenericEndpoint(OrderBaseEndpoint, generics.ListAPIView):
    pass


class OrderRetrieveWithGenericEndpoint(OrderBaseEndpoint, generics.RetrieveAPIView):
    pass


class OrderCreateWithMixinEndpoint(CRUDProxy, OrderBaseEndpoint, GenericAPIView, mixins.CreateModelMixin):
    pass

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class OrderUpdateWithMixinEndpoint(CRUDProxy, OrderBaseEndpoint, GenericAPIView, mixins.UpdateModelMixin):
    pass

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class OrderListWithMixinEndpoint(CRUDProxy, OrderBaseEndpoint, GenericAPIView, mixins.ListModelMixin):
    pass

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class OrderRetrieveWithMixinEndpoint(CRUDProxy, OrderBaseEndpoint, GenericAPIView, mixins.RetrieveModelMixin):
    pass

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class OrderViewset(OrderBaseEndpoint, viewsets.ModelViewSet):
    pass
