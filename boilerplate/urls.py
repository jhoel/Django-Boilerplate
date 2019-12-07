from django.conf.urls import url
from django.urls import include, path
from django.contrib import admin
from django.conf import settings

from core.views import Home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view()),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
