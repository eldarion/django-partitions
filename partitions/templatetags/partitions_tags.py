from django import template

from partitions.utils import chop


register = template.Library()


class PartitionNode(template.Node):
    
    @classmethod
    def handle_token(cls, parser, token):
        bits = token.split_contents()
        if len(bits) != 4:
            raise template.TemplateSyntaxError("Invalid number of arguments.")
        if bits[2] != "using":
            raise template.TemplateSyntaxError("Invalid arguments.")
        return cls(
            queryset = bits[1],
            key = bits[3]
        )
    
    def __init__(self, queryset, key):
        self.queryset = template.Variable(queryset)
        self.key = template.Variable(key)
    
    def render(self, context):
        var_name = self.queryset.var
        queryset = self.queryset.resolve(context)
        key = self.key.resolve(context)
        context[var_name] = chop(queryset, key)
        return ""


@register.tag
def partition(parser, token):
    """
    Usage::
        {% partition queryset using request.get_host %}
    
    Filters the queryset by using rules defined in
    partitions.registry and indexed by the key provided.
    """
    return PartitionNode.handle_token(parser, token)
