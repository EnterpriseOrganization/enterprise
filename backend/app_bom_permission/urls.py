from django.conf.urls import url
from django.conf.urls.static import static
from . import views
from django.conf import settings
urlpatterns = [
    url(r'^$', views.user_login),
    
    
]

urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)