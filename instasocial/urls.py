from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

app_name = 'instaSocial'


urlpatterns = [
    url('^homePage/$', views.homePage, name='homePage'),
    url('^postImage/$', views.postImage, name='postImage'),
    url('^searchUser/$', views.searchUser, name='searchUser'),
    url('^createProfile/$', views.createProfile, name='createProfile'),
    url('^viewProfile/$', views.viewProfile, name='viewProfile'),
    url(r'^signUp/$', views.signUp, name='signUp'),
    url(r'^$', views.logIn, name='logIn'),
    url(r'^logout/$', views.logOut, name='logOut'),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
