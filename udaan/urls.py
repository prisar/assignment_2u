from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic import TemplateView
from django.views.decorators.csrf import ensure_csrf_cookie

urlpatterns = [
    url(r'^$', ensure_csrf_cookie(TemplateView.as_view(template_name="home.html"))),
    url(r'^admin/', admin.site.urls),
    url(r'^auth_api/', include('auth_api.urls')),
    url(r'^booking/', include('booking.urls')),
]
