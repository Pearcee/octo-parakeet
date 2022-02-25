from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls  import  include, url


urlpatterns = [
    
    path('admin/', admin.site.urls),
    url(r'^todo/', include('todo.urls')),
    path("", include("index.urls")),
]

urlpatterns += staticfiles_urlpatterns()
