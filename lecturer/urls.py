from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.lecture, name='lecturer'),
    url(r'^profiles/edit', views.update_user_profile, name='updateuserprofile'),
    url(r'^discover/$', views.discover, name='discover'),
    url(r'^units/(\d+)$', views.units, name='units'),
    url(r'^units/projects/(\d+)$', views.get_unit_projects, name='projects'),
    url(r'^account/(\d+)$', views.account, name='account'),
    url(r'^project/create', views.create_project, name='create_project')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
