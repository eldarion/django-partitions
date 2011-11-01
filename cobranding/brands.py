from django.conf import settings


class Registry(object):
    
    def __init__(self):
        self._brands = {}
    
    def register(self, domain, app_model, expression):
        if not isinstance(app_model, basestring):
            app_model = "%s.%s" % (app_model._meta.app_label, app_model._meta.object_name)
        
        if domain in self._brands:
            raise Exception("'%s' is already registered." % domain)
        if app_model.split(".")[0] not in settings.INSTALLED_APPS:
            raise Exception("'%s' is not in INSTALLED_APPS" % app_model.split(".")[0])
        
        self._brands[domain] = {app_model: expression}
    
    def expression_for(self, domain, app_model):
        return self._brands.get(domain, {}).get(app_model)


registry = Registry()


def register(domain, app_model, expression):
    registry.register(domain, app_model, expression)
