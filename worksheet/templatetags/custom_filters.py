from django import template
register = template.Library()

@register.filter(name='to_negative')
def to_negative(value):
    value = value * (-1)
    return value

@register.filter(name="set_row_class")
def set_row_class(value):
    if value.lower() == 'debit':
        return 'table-warning'
    return 'table-success'

