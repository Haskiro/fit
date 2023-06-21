from .models import Visit
from django.core.cache import cache

def log_visit(request):
    user = request.user if request.user.is_authenticated else None
    visit = {
        "user": user,
        "url": request.path,
        "get_params": request.GET,
        "post_params": request.POST,
        "browser": request.META.get('HTTP_USER_AGENT', ''),
    }
    data = cache.get('visit_log')
    if data:
        data.append(visit)
        cache.set('visit_log', data)
    else:
        cache.set('visit_log', [visit])

def write_visit_log():
    data = cache.get('visit_log')
    print(data)
    if data:
        for visit in data:
            Visit.objects.create(
                user=visit['user'],
                url=visit['url'],
                get_params=visit['get_params'],
                post_params=visit['post_params'],
                browser=visit['browser'],
            )
            cache.delete('visit_log')

def get_visits():
    return Visit.objects.all()