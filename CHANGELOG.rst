Changelog
=========

0.2.0
-----

- BACKWARDS INCOMPATIBLE: Changed ``get_response_data`` method to accept whole serializer class instance instead of its ``data`` attribute

0.1.2
-----

- Fixed ProxiedUpdateModelMixin not having access to ``get_success_headers()``
- Small packaging-related fixes

0.1.0
-----

- Renamed all classes with a ``Proxied`` prefix so they don't get mixed up with DRF's own classes
- Added this changelog

0.0.1
-----

- Initial release
