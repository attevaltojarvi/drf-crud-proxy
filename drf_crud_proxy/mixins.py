from django.http import Http404
from rest_framework import mixins, status
from rest_framework.request import clone_request
from rest_framework.response import Response


class ProxiedListModelMixin(mixins.ListModelMixin):
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            response_serializer = self.get_response_serializer(page, many=True)
            return self.get_paginated_response(response_serializer.data)

        response_serializer = self.get_response_serializer(queryset, many=True)
        return Response(response_serializer.data)


class ProxiedRetrieveModelMixin(mixins.RetrieveModelMixin):
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        response_serializer = self.get_response_serializer(instance)
        return Response(response_serializer.data)


class ProxiedCreateModelMixin(mixins.CreateModelMixin):
    def create(self, request, *args, **kwargs):
        data = self.get_request_data(request)
        request_serializer = self.get_request_serializer(data=data)
        request_serializer.is_valid(raise_exception=True)

        self.perform_create(request_serializer)
        headers = self.get_success_headers(request_serializer.data)

        response_data = self.get_response_data(request_serializer)
        response_serializer = self.get_response_serializer(response_data)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ProxiedUpdateModelMixin(ProxiedCreateModelMixin, mixins.UpdateModelMixin):
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object_or_none()

        # Provide 'PUT-as-create' support
        if instance is None:
            return self.create(request, *args, **kwargs)

        data = self.get_request_data(request)
        request_serializer = self.get_request_serializer(instance, data=data, partial=partial)
        request_serializer.is_valid(raise_exception=True)
        self.perform_update(request_serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        response_data = self.get_response_data(request_serializer)
        response_serializer = self.get_response_serializer(response_data)
        return Response(response_serializer.data)

    def get_object_or_none(self):
        try:
            return self.get_object()
        except Http404:
            if self.request.method == 'PUT':
                # For PUT-as-create operation, we need to ensure that we have
                # relevant permissions, as if this was a POST request.  This
                # will either raise a PermissionDenied exception, or simply
                # return None.
                self.check_permissions(clone_request(self.request, 'POST'))
            else:
                # PATCH requests where the object does not exist should still
                # return a 404 response.
                raise
