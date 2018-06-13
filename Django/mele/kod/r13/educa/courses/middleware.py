from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect
from .models import Course

class SubdomainCourseMiddleware(object):
    """
    Zapewnia obsługę subdomen w aplikacji courses.
    """
    def process_request(self, request):
        host_parts = request.get_host().split('.')
        if len(host_parts) > 2 and host_parts[0] != 'www':
            # Pobranie kursu dla danej subdomeny.
            course = get_object_or_404(Course, slug=host_parts[0])
            course_url = reverse('course_detail',
                                 args=[course.slug])
            # Przekierowanie bieżącego żądania do widoku course_detail.
            url = '{}://{}{}'.format(request.scheme,
                                     '.'.join(host_parts[1:]),
                                     course_url)
            return redirect(url)
