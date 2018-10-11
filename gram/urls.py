from django.conf import settings

from django.conf.urls import url
from . import views

from django.conf.urls.static import static 

urlpatterns=[
    url(r'^$',views.welcome,name = 'welcome'),
    url(r'^search/', views.search_user, name='search_results'),
    # url(r'^signup/$', views.signup, name='signup'),
    url(r'^new/image$', views.new_image, name='new-image'),
    # url(r'^user/(\d+)$', views.profile, name='profile'),
    url(r'^(?P<user_username>\w+)$', views.profile, name='profile'),
    # url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     views.activate, name='activate'),
]

if settings.DEBUG :
    urlpatterns += static (settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)