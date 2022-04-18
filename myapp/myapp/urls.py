from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
    path('blog/', include('blog.urls')),
    path('testcard/', include('testcard.urls')),
    path('todo/', include('todo.urls')),
    path('weather/', include('weather.urls')),
    path("", include("index.urls")),
    path("api/", include("api.urls")),
]

urlpatterns += staticfiles_urlpatterns()
