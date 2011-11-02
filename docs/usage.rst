.. _usage:

Usage
=====

Using ```django-partitions``` starts with registering the models that you want
to apply partitioning, or filtering, to. Somewhere that will get executed when
the server startups up (like urls.py or a models.py) should import and use the
register function::

    from django.db.models import Q
    
    from partitions.registry import register
    
    
    register("partner-a.mycompany.com", "products.Product", Q(partner__slug="partner-a"))
    register("partner-a.mycompany.com", "blog.Post", Q(tags__name__in=["partner", "widget"]))
    register("partner-b.mycompany.com", "products.Product", Q(partner__slug="partner-b"))
    register("partner-b.mycompany.com", "blog.Post", Q(tags__name__in=["partner", "foo"]))


Then to consume this data we can either use a template tag (ideal for external
apps that are not under your control) or call the ```chop``` function with the
same parameters in your ```views.py```.

First the templatetag::

    {% load partitions_tags %}
    ...
    {% partition posts using request.get_host %}


If you control the app, it makes the templates a bit cleaner to use the util
function directly::

    from products.models import Product
    
    from partitions.utils import chop
    
    
    def product_list(request):
        products = Product.objects.all()
        products = chop(products, by=request.get_host())
        ...
