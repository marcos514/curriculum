from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import curriculum.views

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
    url(r'^$', hello.views.curriculum, name='curriculum'),
]
