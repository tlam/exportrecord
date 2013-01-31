from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import redirect


class RequireLoginMiddleware(object):

    def __init__(self):
        self.path_exceptions = (
            reverse('admin:index'),
            reverse('export:login'),
        )

    def process_request(self, request):
        if request.user.is_authenticated():
            return None

        if request.path.replace('/export', '').startswith(self.path_exceptions):
            return None

        return redirect('export:login')
