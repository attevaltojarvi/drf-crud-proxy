from django.shortcuts import get_object_or_404


class CRUDProxy(object):
    def get_serializer_class(self):
        """
        Return the serializer class. Defaults to using `self.serializer_class`.
        You may want to override this if you need to provide different
        serializations depending on the incoming request
        (Eg. admins get full serialization, others get basic serialization).
        """
        assert (
                self.serializer_class is not None or
                getattr(self, 'request_serializer_class', None) is not None
        ), (
                "'%s' should either include one of `serializer_class` and `request_serializer_class` "
                "attribute, or override one of the `get_serializer_class()`, "
                "`get_request_serializer_class()` method."
                % self.__class__.__name__
        )
        return self.serializer_class

    def get_request_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for serializing the incoming request.
        """
        serializer_class = self.get_request_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    def get_request_serializer_class(self):
        """
        Return the serializer class to use for serializing the incoming request.
        Defaults to using `self.request_serializer_class`.
        You may want to override this if you need to provide different
        serializations depending on the incoming request
        (Eg. admins get full serialization, others get basic serialization).
        """
        if getattr(self, 'request_serializer_class', None) is None:
            return self.get_serializer_class()
        return self.request_serializer_class

    def get_response_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating
        and deserializing input.
        """
        serializer_class = self.get_response_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    def get_response_serializer_class(self):
        """
        Return the class to use for the serializer.
        Defaults to using `self.response_serializer_class`.
        You may want to override this if you need to provide different
        serializations depending on the incoming request.
        (Eg. admins can send extra fields, others cannot)
        """
        if getattr(self, 'response_serializer_class', None) is None:
            return self.get_serializer_class()
        return self.response_serializer_class

    def get_request_data(self, request):
        """
        Return the data to be fed to the request serializer. Override to provide custom data.
        """
        return request.data

    def get_response_data(self, serializer):
        """
        Return the data to bed fed to the response serializer. Override to provide custom data.
        """
        return serializer.instance

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())

        # Lookup URL kwarg filter split to own method
        object_filters = self.get_object_filters()

        obj = get_object_or_404(queryset, **object_filters)

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj

    def get_object_filters(self):
        # Perform the lookup filtering
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        if lookup_url_kwarg not in self.kwargs:
            return {}

        return {self.lookup_field: self.kwargs[lookup_url_kwarg]}
