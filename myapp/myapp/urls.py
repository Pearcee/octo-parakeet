from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('todo/', include('todo.urls')),
    path('blog/', include('blog.urls')),
    path("", include("index.urls")),
]

urlpatterns += staticfiles_urlpatterns()
