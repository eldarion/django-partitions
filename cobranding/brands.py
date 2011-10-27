class Registry(object):
    
    def __init__(self):
        self._brands = {}
    
    def register(self, domain, app_model, expression):
        # @@@ Validation: what if it is already registered?
        # @@@ Validation: what if app_model is invalid for INSTALLED_APPS
        # @@@ Validation: what if expression is not a valid Q expression
        if domain not in self._brands:
            self._brands[domain] = {}
        if not isinstance(app_model, basestring):
            app_model = "%s.%s" % (app_model._meta.app_label, app_model._meta.object_name)
        self._brands[domain][app_model] = expression
    
    def expression_for(self, domain, app_model):
        return self._brands.get(domain, {}).get(app_model)


registry = Registry()


def register(domain, app_model, expression):
    registry.register(domain, app_model, expression)
