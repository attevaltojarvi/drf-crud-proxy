"""
Tests for the `drf-rw-serializers` viewsets module.
"""

from django.urls import reverse
from model_mommy import mommy

from test_utils.base_tests import (
    BaseTestCase, TestListRequestSuccess, TestRetrieveRequestSuccess,
    TestCreateRequestSuccess, TestUpdateRequestSuccess)
from example_app.serializers import OrderCreateSerializer, OrderListSerializer


class OrderViewsetListCreateTests(BaseTestCase, TestListRequestSuccess, TestCreateRequestSuccess):
    def setUp(self):
        super(OrderViewsetListCreateTests, self).setUp()
        self.view_url = reverse('viewset_list_create')
        self.list_serializer_class = OrderListSerializer
        self.create_in_serializer_class = OrderCreateSerializer
        self.create_out_serializer_class = OrderListSerializer


class OrderViewsetRetrieveUpdateDestroyTests(BaseTestCase, TestRetrieveRequestSuccess, TestUpdateRequestSuccess):
    def setUp(self):
        super(OrderViewsetRetrieveUpdateDestroyTests, self).setUp()
        self.object = mommy.make('example_app.Order')
        mommy.make('example_app.OrderedProduct', order=self.object, _quantity=2)
        self.view_url = reverse(
            'viewset_retrieve_update_destroy', kwargs={'pk': self.object.pk})
        self.retrieve_serializer_class = OrderListSerializer
        self.update_in_serializer_class = OrderCreateSerializer
        self.update_out_serializer_class = OrderListSerializer
