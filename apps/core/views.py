from django.views.generic import (TemplateView,)

from apps.utilities.decorators import login_required


class IndexView(TemplateView):
    template_name = 'core/index.html'


@login_required
class SecretView(TemplateView):
    """ A view that can only be accessed by an authenticated user """
    template_name = 'core/secret.html'


class AboutView(TemplateView):
    template_name = 'core/about.html'
