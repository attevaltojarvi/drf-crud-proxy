from django.urls import path

from example_app.views import (
    OrderListCreateEndpoint, OrderRetrieveUpdateDestroyEndpoint, OrderRetrieveUpdateEndpoint,
    OrderCreateWithGenericEndpoint, OrderListWithGenericEndpoint, OrderRetrieveWithGenericEndpoint,
    OrderUpdateWithGenericEndpoint, OrderCreateWithMixinEndpoint, OrderUpdateWithMixinEndpoint,
    OrderListWithoutReadSerializerEndpoint, OrderListWithMixinEndpoint, OrderRetrieveWithMixinEndpoint,
    OrderViewset
)


urlpatterns = [
    path(
        'orders-list-without-read-serializer/',
        OrderListWithoutReadSerializerEndpoint.as_view(),
        name='list_without_request_serializer'
    ),
    path(
        r'orders/',
        OrderListCreateEndpoint.as_view(),
        name='list_create'
    ),
    path(
        r'orders/<int:pk>/',
        OrderRetrieveUpdateDestroyEndpoint.as_view(),
        name='retrieve_update_destroy'
    ),
    path(
        r'orders-retrieve-update/<int:pk>/',
        OrderRetrieveUpdateEndpoint.as_view(),
        name='retrieve_update'
    ),
    path(
        r'orders-list-generic-view/',
        OrderListWithGenericEndpoint.as_view(),
        name='list'
    ),
    path(
        r'orders-retrieve-generic-view/<int:pk>/',
        OrderRetrieveWithGenericEndpoint.as_view(),
        name='retrieve'
    ),
    path(
        r'orders-create-generic-view/',
        OrderCreateWithGenericEndpoint.as_view(),
        name='create'
    ),
    path(
        r'orders-update-generic-view/<int:pk>/',
        OrderUpdateWithGenericEndpoint.as_view(),
        name='update'
    ),
    path(
        r'orders-list-mixin/',
        OrderListWithMixinEndpoint.as_view(),
        name='list_mixin'
    ),
    path(
        r'orders-retrieve-mixin/<int:pk>/',
        OrderRetrieveWithMixinEndpoint.as_view(),
        name='retrieve_mixin'
    ),
    path(
        r'orders-create-mixin/',
        OrderCreateWithMixinEndpoint.as_view(),
        name='create_mixin'
    ),
    path(
        r'orders-update-mixin/<int:pk>/',
        OrderUpdateWithMixinEndpoint.as_view(),
        name='update_mixin'
    ),

    path(
        r'orders-viewset/',
        OrderViewset.as_view({
            'get': 'list',
            'post': 'create',
        }),
        name='viewset_list_create'
    ),
    path(
        r'orders-viewset/<int:pk>/',
        OrderViewset.as_view({
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy',
        }),
        name='viewset_retrieve_update_destroy'
    ),
]
