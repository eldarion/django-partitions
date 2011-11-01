from django import template

from cobranding.brands import filter_by_cobrand


register = template.Library()


class CobrandFilterNode(template.Node):

    @classmethod
    def handle_token(cls, parser, token):
        bits = token.split_contents()
        if len(bits) != 4:
            raise template.TemplateSyntaxError("Invalid number of arguments.")
        if bits[2] != "using":
            raise template.TemplateSyntaxError("Invalid arguments.")
        return cls(
            queryset = bits[1],
            hostname = bits[3]
        )

    def __init__(self, queryset, hostname):
        self.queryset = template.Variable(queryset)
        self.hostname = template.Variable(hostname)

    def render(self, context):
        var_name = self.queryset.var
        queryset = self.queryset.resolve(context)
        hostname = self.hostname.resolve(context)

        context[var_name] = filter_by_cobrand(queryset, hostname)
        return ""


@register.tag
def cobrand_filter(parser, token):
    """
    Usage::
        {% cobrand_filter queryset using request.get_host %}

    Filters the queryset by the given hostname using rules defined in
    cobranding.brands.registry
    """
    return CobrandFilterNode.handle_token(parser, token)
