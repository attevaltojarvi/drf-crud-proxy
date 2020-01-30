DRF CRUD Proxy
==============

This package provides extended Django REST Framework generic views and viewsets that provide the possibility to specify
different serializers for reading the incoming request and presenting the response.

This is super handy in situations where you want to, for example, let the user send a ForeignKey attribute,
but present the related object alongside the response instead of only the database ID.

Requirements
------------

- Python 3.6, 3.7, 3.8 (probably older versions as well)
- Django 2.1, 2.2 or 3.0
- Django REST Framework 3.8 or newer, but probably works on any 3.x version

Installation
------------

.. code::

  pip install drf-crud-proxy

Usage
-----

Import the generic views and subclass your own views from them. Specify ``request_serializer_class`` and/or
``response_serializer_class`` to the view (both default to DRF's own ``serializer_class`` attribute).

.. code:: python

  # api/views.py

  from drf_crud_proxy import generics
  from app.models import MyModel
  from api.serializers import MyModelCreateSerializer, MyModelSerializer


  class MyModelListCreateView(generics.ProxiedListCreateAPIView):
      queryset = MyModel.objects.all()
      request_serializer_class = MyModelCreateSerializer
      response_serializer_class = MyModelSerializer

The incoming request is handled with ``MyModelCreateSerializer`` and the response with ``MyModelSerializer``.

If you want to customize the data on either situation, override ``get_request_data`` and/or ``get_response_data``
methods in the view.

The package also supports the so-called ``PUT-as-create`` behavior that was removed from DRF in its 3.0 release. Note that
the user has to have model permissions for the corresponding create behavior (``POST`` request).

**NOTE**: The ``PUT-as-create`` functionality doesn't have tests (yet).

License
-------

MIT

Inspiration
-----------

This functionality in DRF is something I've needed in numerous Django projects, so hopefully this will help someone else
too :)

This package has been built on top of the ideas presented by the great vintasoftware's ``drf-rw-serializers`` (https://github.com/vintasoftware/drf-rw-serializers) package. Thanks!
