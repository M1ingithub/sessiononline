from django import template


register = template.Library()

# not used anywhere, but it works
# adds genericinputbox.html to where ever the tag is applied
# original idea was to add form widgets this way
@register.inclusion_tag("components/genericinputbox.html")
def genericinputbox(title, hint):
    hint = 'Your Name'
    title = 'dsa'
    return {
        'hint' : hint,
        'title' : title,
    }
