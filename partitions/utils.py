from partitions.registry import registry


def chop(queryset, by):
    app_model = "%s.%s" % (
        queryset.model._meta.app_label,
        queryset.model._meta.object_name
    )
    expression = registry.expression_for(by, app_model)
    return queryset.filter(expression) if expression is not None else queryset
