from django.conf import settings


def site_wide(request):
    return {
        'ADMIN_MEDIA_PREFIX': settings.ADMIN_MEDIA_PREFIX,
    }
