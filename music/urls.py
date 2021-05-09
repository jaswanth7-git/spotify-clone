from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.vamshi, name='vamshi'),
    path('music', views.vardhan, name='vardhan'),
      
    path('music/<str:pk>',views.jaswanth, name='jaswanth'),
    path('contact', views.contact, name='contact')
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)


