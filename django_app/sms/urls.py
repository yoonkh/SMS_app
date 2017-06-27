from django.conf.urls import url

from sms import views

urlpatterns = [
    url(r'^$', views.sms_send, name='sms_index')
]