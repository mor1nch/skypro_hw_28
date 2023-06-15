from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from ads import views
from hw_27 import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.StartView.as_view()),
    path("ad/", include("ads.urls")),
    path("cat/", include("categories.urls")),
    path("user/", include("users.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
