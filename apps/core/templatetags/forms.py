from django import template

register = template.Library()


@register.filter()
def field_id(field):
    return field._id_for_label()


@register.inclusion_tag('form_field.html')
def form_field_bare(field, help_text='', initial=None):
    context = form_field(field, help_text, initial)
    context.update({
        'bare': True,
    })
    return context


@register.inclusion_tag('form_field.html')
def form_field(field, help_text='', initial=None, overridden_label=None):
    if help_text:
        field.help_text = help_text
    if initial is not None:
        field.field.initial = initial
    if overridden_label is not None:
        field.label = overridden_label
    return {
        'field': field,
    }


@register.simple_tag
def field_type(field):
    return field.field.widget.__class__.__name__
