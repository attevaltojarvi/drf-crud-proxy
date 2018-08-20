from django.contrib.auth import get_user_model
from model_mommy import mommy
from rest_framework.test import APITestCase, APIClient

from example_app.models import Order
from example_app.serializers import OrderedProductDetailsSerializer


class BaseTestCase(APITestCase):
    def setUp(self):
        self.products = mommy.make('example_app.Product', _quantity=3)

        user_model = get_user_model()

        self.user_email = 'user'
        self.user_password = 'the_password'
        self.user = user_model.objects.create_user(
            username=self.user_email, password=self.user_password)

        self.auth_client = APIClient()
        self.auth_client.force_authenticate(self.user)


class TestListRequestSuccess(object):
    def test_list_request_success(self):
        orders = mommy.make('example_app.Order', _quantity=3)
        for order in orders:
            mommy.make('example_app.OrderedProduct', order=order, _quantity=2)

        response = self.auth_client.get(self.view_url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertCountEqual(
            response.data, self.list_serializer_class(orders, many=True).data)


class TestRetrieveRequestSuccess(object):
    def test_list_request_success(self):
        order = mommy.make('example_app.Order')
        mommy.make('example_app.OrderedProduct', order=order, _quantity=2)
        response = self.auth_client.get(self.view_url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertCountEqual(
            response.data, self.retrieve_serializer_class(order).data)


class TestCreateRequestSuccess(object):
    def test_create_request_success(self):
        data = {
            'customer': 100,
            'ordered_products': [
                {
                    'quantity': 1,
                    'product': self.products[0].id,
                },
                {
                    'quantity': 2,
                    'product': self.products[1].id,
                },
            ],
        }
        response = self.auth_client.post(self.view_url, data, format='json')
        self.assertEqual(response.status_code, 201)
        order = Order.objects.get(id=response.data['id'])
        self.assertEqual(response.data, self.create_out_serializer_class(order).data)
        self.assertEqual(order.customer, data['customer'])

        for ordered_product_dict in data['ordered_products']:
            ordered_product = order.ordered_products.filter(product__id=ordered_product_dict['product']).first()
            self.assertIsNotNone(ordered_product)
            self.assertEqual(ordered_product.quantity, ordered_product_dict['quantity'])


class TestUpdateRequestSuccess(object):
    def test_update_request_success(self):
        data = {
            'customer': 2,
            'ordered_products': [
                {
                    'quantity': 10,
                    'product': self.products[0].id,
                },
                {
                    'quantity': 20,
                    'product': self.products[1].id,
                },
            ]
        }
        response = self.auth_client.put(self.view_url, data, format='json')
        self.object.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.update_out_serializer_class(self.object).data)
        self.assertEqual(self.object.customer, data['customer'])

        for ordered_product_dict in data['ordered_products']:
            ordered_product = self.object.ordered_products.filter(
                product__id=ordered_product_dict['product']).first()
            self.assertIsNotNone(ordered_product)
            self.assertEqual(ordered_product.quantity, ordered_product_dict['quantity'])

    def test_partial_update_customer_request_success(self):
        old_ordered_products = OrderedProductDetailsSerializer(
            self.object.ordered_products.all(), many=True).data

        data = {
            'customer': 2,
        }

        response = self.auth_client.patch(self.view_url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.object.refresh_from_db()
        self.assertEqual(response.data, self.update_out_serializer_class(self.object).data)
        self.assertEqual(self.object.customer, data['customer'])
        self.assertCountEqual(
            OrderedProductDetailsSerializer(self.object.ordered_products.all(), many=True).data,
            old_ordered_products)

    def test_partial_update_ordered_products_request_success(self):
        old_customer = self.object.customer
        data = {
            'ordered_products': [
                {
                    'quantity': 10,
                    'product': self.products[2].id,
                },
            ]
        }
        response = self.auth_client.patch(self.view_url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.object.refresh_from_db()
        self.assertEqual(response.data, self.update_out_serializer_class(self.object).data)
        for ordered_product_dict in data['ordered_products']:
            ordered_product = self.object.ordered_products.filter(
                product__id=ordered_product_dict['product']).first()
            self.assertIsNotNone(ordered_product)
            self.assertEqual(ordered_product.quantity, ordered_product_dict['quantity'])
        self.assertEqual(self.object.customer, old_customer)
