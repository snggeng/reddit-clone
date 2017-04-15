from django.conf.urls import url

import views

urlpatterns = [
    url(r'create$', views.createpost),
    url(r'upvote/(?P<pid>\d{1,4})$', views.upvote),
]
