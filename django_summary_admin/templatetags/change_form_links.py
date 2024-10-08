from django.contrib.admin.templatetags.base import InclusionAdminNode
from django.template import Library

register = Library()


def function(context):
    return context

@register.tag(name="change_form_object_tools_links")
def change_form_object_tools_links_tag(parser, token):
    return InclusionAdminNode(
        parser,
        token,
        func=function,
        template_name="../change_links/change_form_object_tools_links.html",
    )
