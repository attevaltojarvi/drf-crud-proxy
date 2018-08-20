"""
Tests for the `drf-rw-serializers` mixins module.
"""

from django.urls import reverse
from model_mommy import mommy

from test_utils.base_tests import (
    BaseTestCase, TestListRequestSuccess, TestRetrieveRequestSuccess,
    TestCreateRequestSuccess, TestUpdateRequestSuccess
)
from example_app.serializers import OrderCreateSerializer, OrderListSerializer


class OrderCreateWithMixinEndpointTests(BaseTestCase, TestCreateRequestSuccess):
    def setUp(self):
        super(OrderCreateWithMixinEndpointTests, self).setUp()
        self.view_url = reverse('create_mixin')
        self.list_serializer_class = OrderListSerializer
        self.create_in_serializer_class = OrderCreateSerializer
        self.create_out_serializer_class = OrderListSerializer


class OrderUpdateWithMixinEndpointTests(BaseTestCase, TestUpdateRequestSuccess):
    def setUp(self):
        super(OrderUpdateWithMixinEndpointTests, self).setUp()
        self.object = mommy.make('example_app.Order')
        mommy.make('example_app.OrderedProduct', order=self.object, _quantity=2)
        self.view_url = reverse('update_mixin', kwargs={'pk': self.object.pk})
        self.retrieve_serializer_class = OrderListSerializer
        self.update_in_serializer_class = OrderCreateSerializer
        self.update_out_serializer_class = OrderListSerializer


class OrderListWithMixinEndpointTests(BaseTestCase, TestListRequestSuccess):
    def setUp(self):
        super(OrderListWithMixinEndpointTests, self).setUp()
        self.view_url = reverse('list_mixin')
        self.list_serializer_class = OrderListSerializer


class OrderRetrieveWithMixinEndpointTests(BaseTestCase, TestRetrieveRequestSuccess):
    def setUp(self):
        super(OrderRetrieveWithMixinEndpointTests, self).setUp()
        self.object = mommy.make('example_app.Order')
        mommy.make('example_app.OrderedProduct', order=self.object, _quantity=2)
        self.view_url = reverse('retrieve_mixin', kwargs={'pk': self.object.pk})
        self.retrieve_serializer_class = OrderListSerializer
