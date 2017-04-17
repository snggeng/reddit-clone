from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import views

urlpatterns = [
    url(r'create$', views.createpost),
    url(r'upvote/(?P<pid>\d{1,4})$', views.upvote),
]

urlpatterns += staticfiles_urlpatterns()
