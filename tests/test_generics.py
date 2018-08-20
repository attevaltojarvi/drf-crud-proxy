"""
Tests for the `drf-rw-serializers` generics module.
"""

from django.urls import reverse
from model_mommy import mommy

from test_utils.base_tests import (
    BaseTestCase, TestListRequestSuccess, TestRetrieveRequestSuccess,
    TestCreateRequestSuccess, TestUpdateRequestSuccess
)
from example_app.serializers import OrderCreateSerializer, OrderListSerializer


class OrderListCreateEndpointTests(
        BaseTestCase, TestListRequestSuccess, TestCreateRequestSuccess):

    def setUp(self):
        super(OrderListCreateEndpointTests, self).setUp()
        self.view_url = reverse('list_create')
        self.list_serializer_class = OrderListSerializer
        self.create_in_serializer_class = OrderCreateSerializer
        self.create_out_serializer_class = OrderListSerializer


class OrderRetrieveUpdateDestroyEndpointTests(
        BaseTestCase, TestRetrieveRequestSuccess, TestUpdateRequestSuccess):

    def setUp(self):
        super(OrderRetrieveUpdateDestroyEndpointTests, self).setUp()
        self.object = mommy.make('example_app.Order')
        mommy.make('example_app.OrderedProduct', order=self.object, _quantity=2)
        self.view_url = reverse('retrieve_update_destroy', kwargs={'pk': self.object.pk})
        self.retrieve_serializer_class = OrderListSerializer
        self.update_in_serializer_class = OrderCreateSerializer
        self.update_out_serializer_class = OrderListSerializer


class OrderListWithoutReadSerializerEndpointTests(
        BaseTestCase, TestListRequestSuccess):

    def setUp(self):
        super(OrderListWithoutReadSerializerEndpointTests, self).setUp()
        self.view_url = reverse('list_without_request_serializer')
        self.list_serializer_class = OrderListSerializer


class OrderRetrieveUpdateEndpointTests(
        BaseTestCase, TestRetrieveRequestSuccess, TestUpdateRequestSuccess):

    def setUp(self):
        super(OrderRetrieveUpdateEndpointTests, self).setUp()
        self.object = mommy.make('example_app.Order')
        mommy.make('example_app.OrderedProduct', order=self.object, _quantity=2)
        self.view_url = reverse('retrieve_update', kwargs={'pk': self.object.pk})
        self.retrieve_serializer_class = OrderListSerializer
        self.update_in_serializer_class = OrderCreateSerializer
        self.update_out_serializer_class = OrderListSerializer


class OrderCreateWithGenericEndpointTests(BaseTestCase, TestCreateRequestSuccess):

    def setUp(self):
        super(OrderCreateWithGenericEndpointTests, self).setUp()
        self.view_url = reverse('create')
        self.list_serializer_class = OrderListSerializer
        self.create_in_serializer_class = OrderCreateSerializer
        self.create_out_serializer_class = OrderListSerializer


class OrderUpdateWithGenericEndpointTests(BaseTestCase, TestUpdateRequestSuccess):

    def setUp(self):
        super(OrderUpdateWithGenericEndpointTests, self).setUp()
        self.object = mommy.make('example_app.Order')
        mommy.make('example_app.OrderedProduct', order=self.object, _quantity=2)
        self.view_url = reverse('update', kwargs={'pk': self.object.pk})
        self.retrieve_serializer_class = OrderListSerializer
        self.update_in_serializer_class = OrderCreateSerializer
        self.update_out_serializer_class = OrderListSerializer


class OrderListWithGenericEndpointTests(BaseTestCase, TestListRequestSuccess):

    def setUp(self):
        super(OrderListWithGenericEndpointTests, self).setUp()
        self.view_url = reverse('list')
        self.list_serializer_class = OrderListSerializer


class OrderRetrieveWithGenericEndpointTests(BaseTestCase, TestRetrieveRequestSuccess):

    def setUp(self):
        super(OrderRetrieveWithGenericEndpointTests, self).setUp()
        self.object = mommy.make('example_app.Order')
        mommy.make('example_app.OrderedProduct', order=self.object, _quantity=2)
        self.view_url = reverse('retrieve', kwargs={'pk': self.object.pk})
        self.retrieve_serializer_class = OrderListSerializer
