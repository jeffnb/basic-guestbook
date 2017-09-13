from django.conf.urls import url

from adv.views import SigninListView, SigninCreateView

urlpatterns = [
    url(r'^$', SigninListView.as_view()),
    url(r'^create/$', SigninCreateView.as_view())

]