.. _templatetags:


Template Tags
=============

partition
---------

This will add additional filtering to the query given a string used to lookup
the registery Q expression for the key and model (same model as queryset)::

    {% partition queryset using request.get_host %}

