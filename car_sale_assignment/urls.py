from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main, name='main'),

    path('brands/<slug:brand_slug>/', views.main, name='brand_wise_car'),
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('brand/', include('brand.urls')),
    path('car/', include('car.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)