from django.conf.urls import url

import views

urlpatterns = [
    url(r'create$', views.createpost),
    url(r'upvote/(?<pid>\d{0,4})', views.upvote),
]
