from django.template import Library

from Courses.models import subscribe

register = Library()


@register.simple_tag
def load_user_courses(user):
    registrations = subscribe.objects.order_by('-id').filter(user=user)
    return registrations
    

@register.inclusion_tag('partials/_my_courses.html')
def user_courses(user):
    registrations = subscribe.objects.order_by('-id').filter(user=user)
    return {'registrations': registrations}
