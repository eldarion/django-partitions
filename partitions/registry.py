from django.conf import settings


class Registry(object):
    
    def __init__(self):
        self._partitions = {}
    
    def register(self, key, app_model, expression):
        if not isinstance(app_model, basestring):
            app_model = "%s.%s" % (
                app_model._meta.app_label,
                app_model._meta.object_name
            )
        
        if key in self._partitions and app_model in self._partitions[key]:
            raise Exception("'%s' is already registered." % key)
        if app_model.split(".")[0] not in settings.INSTALLED_APPS:
            raise Exception("'%s' is not in INSTALLED_APPS" % app_model.split(".")[0])
        
        if key in self._partitions:
            self._partitions[key].update({app_model: expression})
        else:
            self._partitions[key] = {app_model: expression}
    
    def expression_for(self, key, app_model):
        return self._partitions.get(key, {}).get(app_model)


registry = Registry()


def register(key, app_model, expression):
    registry.register(key, app_model, expression)
