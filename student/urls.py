from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.student, name='student'),
    url(r'^profiles/edit', views.update_user_profile, name='updateuserprofile'),
    url(r'^student_account/(\d+)$', views.account, name='student_account'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
