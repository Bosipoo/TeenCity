from django.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('teenapp.urls')),
    path('',include('django.contrib.auth.urls')),
]

#Customizing Admin Texts
admin.site.site_header = 'TeenCity'
admin.site.index_title = 'Welcome to TeenCity Admin'
admin.site.site_title = 'Control Panel'