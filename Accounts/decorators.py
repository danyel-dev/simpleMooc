from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages

from Courses.models import Course, subscribe


def subscription_required(detail_advert):
    def wrapper(request, *args, **kwargs):
        slug = kwargs.get('slug')
        course = get_object_or_404(Course, slug_course=slug)

        try:    
            subscriber = get_object_or_404(subscribe, user=request.user, course=course)
        except:
            messages.error(request, 'Desculpe, mas você não tem permissão para acessar essa página')
            return redirect('dashboard')

        if not subscriber.is_approved():
            messages.error(request, 'A sua inscrição no curso ainda está pendente')
            return redirect('dashboard')

        request.course = course
        return detail_advert(request, *args, **kwargs)

    return wrapper
