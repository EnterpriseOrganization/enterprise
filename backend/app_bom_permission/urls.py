from django.conf.urls import url
from django.conf.urls.static import static
from . import views
from django.conf import settings
urlpatterns = [
    url(r'^login', views.user_login),
    url(r'^getUser',views.get_user)
    
]

urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)